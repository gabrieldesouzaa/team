// =====================
// 1. Configure handbook
// =====================

const HANDBOOK_TEXT = `
[PASTE YOUR MOCK COMPANY HANDBOOK TEXT HERE]

For example:
- Work hours, PTO, holidays
- Dress code
- Remote work policy
- Equipment & IT usage
- Code of conduct
- Benefits & payroll
`.trim();

// Optional: customize these bits of wording
const COMPANY_NAME = "Your Company Name";
const DENY_MESSAGE =
  "I’m only able to help with questions about new employee onboarding and official company policies. " +
  "For other topics, please contact the appropriate person or use another resource.";

// =====================
// 2. Shared helpers
// =====================

const chatLog = document.getElementById("chat-log");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

// Set current date/time in the date divider
function updateDateDivider() {
  const dateDivider = document.getElementById("date-divider");
  const now = new Date();
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  dateDivider.textContent = now.toLocaleDateString('en-US', options);
}

updateDateDivider();

function appendMessage(sender, text, options = {}) {
  const wrapper = document.createElement("div");
  wrapper.className = `message ${sender}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";

  if (options.isTemporary) {
    bubble.dataset.temp = "true";
  }

  bubble.textContent = text;
  wrapper.appendChild(bubble);
  chatLog.appendChild(wrapper);

  chatLog.scrollTop = chatLog.scrollHeight;
}

function replaceLastTempBotMessage(text) {
  const bubbles = chatLog.querySelectorAll(".message.bot .bubble");
  for (let i = bubbles.length - 1; i >= 0; i--) {
    const bubble = bubbles[i];
    if (bubble.dataset.temp === "true") {
      bubble.textContent = text;
      delete bubble.dataset.temp;
      chatLog.scrollTop = chatLog.scrollHeight;
      return;
    }
  }
  appendMessage("bot", text);
}

// Build a single system prompt string we can reuse for both providers
function getSystemPrompt() {
  return `
You are a helpful HR onboarding assistant for ${COMPANY_NAME}.

SCOPE:
- You are ONLY allowed to answer questions about:
  (a) new employee onboarding at ${COMPANY_NAME}, and
  (b) official company policies.
- If the user asks anything outside that scope (for example: personal questions, world knowledge,
  technical questions unrelated to onboarding/policy, sports, politics, etc.), you MUST NOT answer.
  Instead, respond with this exact message (and nothing else):

  "${DENY_MESSAGE}"

KNOWLEDGE SOURCE:
- Use ONLY the information from the company handbook below.
- If the user asks about something that is not covered or not clear in the handbook, say you don't know
  and suggest they contact HR or their manager.
- Do NOT invent policies or make assumptions that are not supported by the handbook.

STYLE:
- Be concise and clear.
- When relevant, refer to specific sections or headings from the handbook if they exist.

COMPANY HANDBOOK:
"""${HANDBOOK_TEXT}"""
  `.trim();
}

// Initial greeting
appendMessage(
  "bot",
  "Ask a question about company policy, or your personal data, and I will answer the best I can!"
);

// =====================
// 3. OpenAI API call
// =====================

async function callOpenAI(apiKey, userMessage) {
  const endpoint = "https://api.openai.com/v1/chat/completions";
  const systemPrompt = getSystemPrompt();

  const body = {
    model: "gpt-4o-mini",
    temperature: 0.2,
    messages: [
      { role: "system", content: systemPrompt },
      { role: "user", content: userMessage },
    ],
  };

  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify(body),
  });

  const data = await response.json();

  if (!response.ok) {
    const message =
      (data && data.error && data.error.message) ||
      `OpenAI request failed with status ${response.status}`;
    throw new Error(message);
  }

  const reply =
    data.choices && data.choices[0] && data.choices[0].message.content;
  return (reply || "").trim();
}

// =====================
// 4. Gemini API call
// =====================
// Uses REST generateContent endpoint:
// POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent
// Header: x-goog-api-key: YOUR_API_KEY
// Body: { system_instruction, contents } :contentReference[oaicite:2]{index=2}

async function callGemini(apiKey, userMessage) {
  const endpoint =
    "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent";
  const systemPrompt = getSystemPrompt();

  const payload = {
    system_instruction: {
      parts: [{ text: systemPrompt }],
    },
    contents: [
      {
        role: "user",
        parts: [{ text: userMessage }],
      },
    ],
  };

  const response = await fetch(endpoint, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-goog-api-key": apiKey,
    },
    body: JSON.stringify(payload),
  });

  const data = await response.json();

  if (!response.ok) {
    const message =
      (data && data.error && (data.error.message || data.error.status)) ||
      `Gemini request failed with status ${response.status}`;
    throw new Error(message);
  }

  // Typical Gemini generateContent response:
  // data.candidates[0].content.parts[0].text :contentReference[oaicite:3]{index=3}
  const candidates = data.candidates || [];
  const first = candidates[0];
  const parts = first && first.content && first.content.parts;
  const text = parts && parts[0] && parts[0].text;
  return (text || "").trim();
}

// =====================
// 5. Form submit handler
// =====================

chatForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const text = userInput.value.trim();

  if (!text) return;

  appendMessage("user", text);
  userInput.value = "";
  userInput.focus();

  appendMessage("bot", "Thinking...", { isTemporary: true });
  chatForm.querySelector(".send-btn").disabled = true;

  try {
    // This is where you would call your backend API
    // For now, we'll just simulate a response
    const reply = "This is a demo response. Connect this to your backend API.";
    
    setTimeout(() => {
      replaceLastTempBotMessage(reply);
      chatForm.querySelector(".send-btn").disabled = false;
    }, 1000);
  } catch (err) {
    console.error(err);
    replaceLastTempBotMessage(
      "Sorry, I ran into an error. Please try again."
    );
    chatForm.querySelector(".send-btn").disabled = false;
  }
});

// Add refresh button functionality
document.getElementById("refresh-btn").addEventListener("click", () => {
  if (confirm("Are you sure you want to refresh the chat? This will clear all messages.")) {
    chatLog.innerHTML = "";
    appendMessage(
      "bot",
      "Ask a question about company policy, or your personal data, and I will answer the best I can!"
    );
  }
});

// Add minimize button functionality
document.getElementById("minimize-btn").addEventListener("click", () => {
  alert("In a production app, this would minimize the chat widget.");
});
