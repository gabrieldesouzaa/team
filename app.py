import streamlit as st
import google.generativeai as genai
import os

# Configure the Gemini API
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    st.error(
        "🚨 Configuration Error: Please set `GEMINI_API_KEY`."
    )
    st.stop()

genai.configure(api_key=API_KEY)
MODEL_ID = "gemini-2.0-flash-001" 

# Load Company Policy and System Instruction from files
try:
    with open("company_policy.md", "r") as f:
        COMPANY_POLICY = f.read()
except FileNotFoundError:
    st.error("`company_policy.md` not found.")
    st.stop()

try:
    with open("system_instruction.txt", "r") as f:
        SYSTEM_INSTRUCTION_TEMPLATE = f.read()
except FileNotFoundError:
    st.error("`system_instruction.txt` not found.")
    st.stop()

SYSTEM_INSTRUCTION = SYSTEM_INSTRUCTION_TEMPLATE.format(company_policy=COMPANY_POLICY)

import json

# Chat History Management
CHAT_HISTORY_FILE = "chat_history.json"

def save_chat_history(messages):
    """Saves the chat history to a JSON file."""
    with open(CHAT_HISTORY_FILE, "w") as f:
        json.dump(messages, f)

def load_chat_history():
    """Loads the chat history from a JSON file."""
    if os.path.exists(CHAT_HISTORY_FILE):
        with open(CHAT_HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

# Streamlit UI
# Custom CSS for fine-tuning elements
st.markdown("""
    <style>
        .title-container h1 {
            font-size: 2.5em;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
        }
        .title-container p {
            font-size: 1.1em;
        }
    </style>
""", unsafe_allow_html=True)

# Custom Title
st.markdown("""
<div class="title-container">
    <h1>Onboarding HR Assistant</h1>
    <p>Your friendly guide to company policies</p>
</div>
""", unsafe_allow_html=True)


if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=SYSTEM_INSTRUCTION
    )
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

for message in st.session_state.messages:
    avatar = "🧑" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        if "content" in message:
            st.markdown(message["content"])
        if "files" in message:
            for file_name, file_data in message["files"].items():
                if "image" in file_data["type"]:
                    st.image(file_data["data"], caption=file_name, width=200)
                else:
                    st.write(f"📄 {file_name}")

# Text input
st.markdown("### 💬 Ask a Question")
prompt = st.text_input(
    "Enter your question:",
    placeholder="e.g., How many PTO days can I get?",
    help="Type your question and press Enter to get an answer"
)

# Button
if st.button("Generate"): 
    if prompt:
        try:
            model_for_prompt = genai.GenerativeModel(MODEL_ID)
            response = model_for_prompt.generate_content(contents=prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt.")


# File uploader for images and documents
uploaded_files = st.file_uploader(
    "📎",
    accept_multiple_files=True,
    label_visibility="collapsed",
    key="animated_uploader"
)

# history management to prevent infinite growth
MAX_HISTORY = 50

if len(st.session_state.messages) > MAX_HISTORY:
    st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]
    save_chat_history(st.session_state.messages)

def validate_input(user_input):
    """Basic input validation"""
    if not user_input or user_input.strip() == "":
        return False, "Type your question here."
    if len(user_input) > 1000:
        return False, "Question too long. Please keep under 1000 characters."
    return True, ""


# Clear history button
if st.button("Clear History", type="secondary"):
    st.session_state.messages = []
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.auto_question = ""
    if os.path.exists(CHAT_HISTORY_FILE):
        os.remove(CHAT_HISTORY_FILE)
    st.rerun()
