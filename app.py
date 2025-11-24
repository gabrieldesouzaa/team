import streamlit as st
import google.generativeai as genai
import os
import PIL.Image
import io

# Configure the Gemini API
API_KEY = os.environ.get("GEMINI_API_KEY")

if not API_KEY:
    st.error(
        "🚨 Configuration Error: Please set `GEMINI_API_KEY`."
    )
    st.stop()

genai.configure(api_key=API_KEY)

MODEL_ID = "gemini-2.0-flash-001" 


COMPANY_POLICY = """
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
"""

SYSTEM_INSTRUCTION = f"""You are an expert HR assistant for "Innovate Inc.". Your sole purpose is to answer employee questions about the company policy. 
You must base your answers strictly and exclusively on the provided company policy document. 
If a user uploads a file, you can also answer questions about it.
Do not use any external knowledge or make assumptions. 
If a question cannot be answered from the policy or the file, state that the information is not available in the provided documents and do not apologize. 
Keep your answers concise, clear, and professional. Format your answers using markdown for better readability where appropriate (e.g., lists, bold text).

Here is the company policy:
---
{COMPANY_POLICY}
---
"""

# --- Streamlit UI ---

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
    st.session_state.messages = []

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

# Consolidate input area
with st.container():
    col1, col2 = st.columns([1, 10])
    with col1:
        uploaded_files = st.file_uploader(
            "📎", accept_multiple_files=True, label_visibility="collapsed"
        )
    with col2:
        if "auto_question" in st.session_state and st.session_state.auto_question:
            user_input = st.chat_input("Ask about company policy...", key="auto_question_input")
            st.session_state.auto_question = "" # Reset
        else:
            user_input = st.chat_input("Enter your question here...")

st.markdown("""
<style>
    @keyframes bounce {
        0%, 20%, 60%, 100% { transform: translateY(0); }
        40% { transform: translateY(-5px); }
        80% { transform: translateY(-2px); }
    }
    
    .animated-paperclip {
        width: 40px !important;
    }
    .animated-paperclip button {
        width: 40px !important;
        height: 40px !important;
        min-height: 40px !important;
        padding: 0 !important;
        border-radius: 10px !important;
        background: linear-gradient(45deg, #FFD700, #FFA500) !important;
        border: none !important;
        color: white !important;
        font-size: 16px !important;
        transition: all 0.3s ease !important;
    }
    .animated-paperclip button:hover {
        animation: bounce 0.6s ease;
        background: linear-gradient(45deg, #FFA500, #FF8C00) !important;
    }
</style>
""", unsafe_allow_html=True)

uploaded_files = st.file_uploader(
    "📎",
    accept_multiple_files=True,
    label_visibility="collapsed",
    key="animated_uploader"
)

if user_input:
    message_content = {"role": "user", "content": user_input, "files": {}}
    
    if uploaded_files:
        for uploaded_file in uploaded_files:
            bytes_data = uploaded_file.read()
            message_content["files"][uploaded_file.name] = {
                "type": uploaded_file.type,
                "data": bytes_data
            }

    st.session_state.messages.append(message_content)

    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)
        if uploaded_files:
            for file_name, file_data in message_content["files"].items():
                if "image" in file_data["type"]:
                    st.image(file_data["data"], caption=file_name, width=200)
                else:
                    st.write(f"📄 {file_name}")


    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            try:
                contents = [user_input]
                if uploaded_files:
                    for uploaded_file in uploaded_files:
                        if "image" in uploaded_file.type:
                            img = PIL.Image.open(io.BytesIO(message_content["files"][uploaded_file.name]["data"]))
                            contents.append(img)
                        else: # For now, treat other files as text
                            contents.append(message_content["files"][uploaded_file.name]["data"].decode())
                
                response = st.session_state.chat_session.send_message(contents)
                assistant_response = response.text
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

# Add history management to prevent infinite growth
MAX_HISTORY = 50

if len(st.session_state.messages) > MAX_HISTORY:
    st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]

def validate_input(user_input):
    """Basic input validation"""
    if not user_input or user_input.strip() == "":
        return False, "Type your question here."
    if len(user_input) > 1000:
        return False, "Question too long. Please keep under 1000 characters."
    return True, ""


# Clear chat button
if st.button("Clear Chat", type="secondary"):
    st.session_state.messages = []
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.auto_question = ""
    st.rerun()
