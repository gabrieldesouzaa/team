import streamlit as st
import os
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

import google.generativeai as genai

load_dotenv()

# --- CSS from style.css (embedded) ---
st.markdown("""
<style>
* { box-sizing: border-box; }
body {
  margin: 0; font-family: system-ui, -apple-system, sans-serif;
  background: #f3f4f6; display: flex; justify-content: center;
  align-items: center; min-height: 100vh;
}
.app-container {
  background: #ffffff; width: 100%; max-width: 800px; height: 90vh;
  border-radius: 16px; box-shadow: 0 10px 30px rgba(15, 23, 42, 0.12);
  display: flex; flex-direction: column; overflow: hidden;
}
.app-header {
  padding: 16px 20px; border-bottom: 1px solid #e5e7eb;
  background: linear-gradient(135deg, #2563eb, #3b82f6); color: white;
}
.app-header h1 { margin: 0 0 4px; font-size: 1.3rem; }
.app-header p { margin: 0; opacity: 0.9; font-size: 0.9rem; }
/* Streamlit Specific Overrides */
div.stApp > header { display: none; }
.stChatMessage { background: none !important; }
</style>
""", unsafe_allow_html=True)

# --- Constants ---
HANDBOOK_TEXT = """
- Work hours: 9 AM to 5 PM, Monday to Friday.
- PTO: 20 days per year.
- Holidays: All major US holidays are observed.
- Dress code: Business casual.
- Remote work: Permitted two days a week.
- IT usage: Company equipment is for business purposes only.
""".strip()
COMPANY_NAME = "FutureCorp"
DENY_MESSAGE = (
    "I can only answer questions about new employee onboarding and official company policies. "
    "For other topics, please contact HR."
)
MODEL_ID = "gemini-2.5-flash"

# --- System Prompt ---
def get_system_prompt():
    return f"""
You are an HR onboarding assistant for {COMPANY_NAME}. Your scope is to ONLY answer questions about new employee onboarding and the official company policies detailed in the handbook below. If asked anything else, you MUST respond with: "{DENY_MESSAGE}"

COMPANY HANDBOOK:
---
{HANDBOOK_TEXT}
---
""".strip()

# --- Gemini API Configuration ---
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set")
genai.configure(api_key=api_key)
model = genai.GenerativeModel(MODEL_ID)

# --- Streamlit UI ---
st.set_page_config(layout="centered", page_title=f"{COMPANY_NAME} Onboarding")

# Custom HTML Structure
st.markdown(f"""
<div class="app-container">
    <header class="app-header">
        <h1>Onboarding Assistant</h1>
        <p>Ask about new-hire onboarding and company policies</p>
    </header>
""", unsafe_allow_html=True)

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add initial greeting if history is empty
if not st.session_state.messages:
     initial_greeting = f"Hi! I’m your {COMPANY_NAME} onboarding assistant. How can I help you today?"
     st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Ask about company policies..."):
    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Prepare conversation history for the API
    # Prepend system prompt as first message
    api_history = [
        {"role": "user", "parts": [get_system_prompt()]}
    ] + [
        {"role": "user" if msg["role"] == "user" else "model", "parts": [msg["content"]]}
        for msg in st.session_state.messages
    ]

    # Get response from Gemini
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        try:
            response = model.generate_content(
                api_history,
                generation_config={
                    "temperature": 0.4,
                    "max_output_tokens": 512,
                },
                safety_settings={
                    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                },
            )
            full_response = response.text
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
            full_response = "Sorry, I ran into an error. Please try again."
            message_placeholder.markdown(full_response)
    
    # Add assistant response to display history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Close the main app div
st.markdown('</div>', unsafe_allow_html=True)
