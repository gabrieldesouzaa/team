import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from google.generativeai.types import HarmCategory, HarmBlockThreshold

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

COMPANY_NAME = "Innovate Inc."

try:
    with open("system_instruction.txt", "r") as f:
        SYSTEM_INSTRUCTION_TEMPLATE = f.read()
except FileNotFoundError:
    st.error("`system_instruction.txt` not found.")
    st.stop()

SYSTEM_INSTRUCTION = SYSTEM_INSTRUCTION_TEMPLATE.format(company_policy=COMPANY_POLICY)

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash-001',
    system_instruction=SYSTEM_INSTRUCTION
)

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

# Initialize chat history in session state if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add initial greeting if history is empty
if not st.session_state.messages:
    initial_greeting = f"Hi! I’m your {COMPANY_NAME} onboarding assistant. How can I help you today?"
    st.session_state.messages.append({"role": "assistant", "content": initial_greeting})

# If the user requested to edit personal info (via /edit), show the edit form in the main area
if st.session_state.get("_edit_personal") and st.session_state.get("auth_ok") and st.session_state.get("auth_user"):
    personal = load_personal_data()
    me = personal.get(st.session_state.auth_user, {})
    with st.form("update_personal"):
        new_email = st.text_input("Email", value=me.get("email", ""))
        new_phone = st.text_input("Phone", value=me.get("phone", ""))
        new_state = st.text_input("State", value=me.get("state", ""))
        new_address = st.text_input("Home Address", value=me.get("home_address", ""))
        new_pay_rate = st.text_input("Pay Rate", value=str(me.get("pay_rate", "")))
        new_hours_pto = st.number_input("Hours PTO", value=int(me.get("hours_pto", 0)))
        new_hours_sick = st.number_input("Hours Sick Time", value=int(me.get("hours_sick_time", 0)))
        new_employee_number = st.text_input("Employee Number", value=me.get("employee_number", ""))
        new_job_title = st.text_input("Job Title", value=me.get("job_title", ""))
        new_disability = st.text_input("Disability", value=me.get("disability", ""))
        if st.form_submit_button("Save"):
            personal[st.session_state.auth_user] = {
                "email": new_email,
                "phone": new_phone,
                "state": new_state,
                "home_address": new_address,
                "pay_rate": new_pay_rate,
                "hours_pto": int(new_hours_pto),
                "hours_sick_time": int(new_hours_sick),
                "employee_number": new_employee_number,
                "job_title": new_job_title,
                "disability": new_disability,
            }
            save_personal_data(personal)
            st.success("Saved.")
            st.session_state._edit_personal = False

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

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


# File uploader for images and documents
uploaded_files = st.file_uploader(
    "📎",
    accept_multiple_files=True,
    label_visibility="collapsed",
    key="animated_uploader"
)

# Clear history button
if st.button("Clear History", type="secondary"):
    st.session_state.messages = []
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.auto_question = ""
    if os.path.exists(CHAT_HISTORY_FILE):
        os.remove(CHAT_HISTORY_FILE)
    st.rerun()
