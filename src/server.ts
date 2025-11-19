import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import { GoogleGenerativeAI, ChatSession } from '@google/generative-ai';

dotenv.config();

const app = express();
const port = process.env.PORT || 5000;

app.use(cors());
app.use(express.json());

const COMPANY_POLICY = `
# Innovate Inc. Company Policy

## 1.  Work Hours
-   Standard work hours are 9:00 AM to 5:00 PM, Monday to Friday.
-   Flexible working hours can be arranged with your manager.

## 2.  Paid Time Off (PTO)
-   Employees receive 20 days of PTO per year.
-   PTO requests must be submitted at least two weeks in advance.

## 3.  Code of Conduct
-   All employees are expected to maintain a professional and respectful work environment.
-   Harassment of any kind will not be tolerated.
`;

let ai: GoogleGenerativeAI;
const getAi = () => {
  if (!ai) {
    const apiKey = process.env.GEMINI_API_KEY;
    if (!apiKey) {
      throw new Error("API_KEY environment variable not set.");
    }
    ai = new GoogleGenerativeAI(apiKey);
  }
  return ai;
};

const createChatSession = (): ChatSession => {
    const genAI = getAi();
  
    const systemInstruction = `You are an expert HR assistant for "Innovate Inc.". Your sole purpose is to answer employee questions about the company policy. 
    You must base your answers strictly and exclusively on the provided company policy document. 
    Do not use any external knowledge or make assumptions. 
    If a question cannot be answered from the policy, state that the information is not available in the policy document and do not apologize. 
    Keep your answers concise, clear, and professional. Format your answers using markdown for better readability where appropriate (e.g., lists, bold text).
  
    Here is the company policy:
    ---
    ${COMPANY_POLICY}
    ---
    `;
  
    const chat = genAI.getGenerativeModel({
        model: 'gemini-1.5-flash',
        systemInstruction: systemInstruction,
      }).startChat({
        history: [],
      });
  
    return chat;
  };

let chat: ChatSession;

app.post('/api/chat', async (req, res) => {
    const userMessage = req.body.message;

    if (!userMessage) {
        return res.status(400).json({ error: 'No message provided' });
    }

    try {
        if (!chat) {
            chat = createChatSession();
        }
        const result = await chat.sendMessage(userMessage);
        const response = await result.response;
        const text = response.text();
        res.json({ reply: text });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to get response from AI' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
