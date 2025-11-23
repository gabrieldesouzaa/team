import streamlit as st
import google.generativeai as genai
import os
import PIL.Image
import io

# Set up Google Generative AI
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
except KeyError:
    st.error("GEMINI_API_KEY environment variable not set. Please add it to your Streamlit secrets.")
    st.stop()

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
            font-size: 2.5em; /* Make the title bigger */
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3); /* Add a subtle shadow */
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
    <p>Your friendly guide to company policies at Innovate Inc.</p>
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

# --- Sidebar Content ---
with st.sidebar:
    st.subheader("Example Questions")
    
    st.markdown("""
    This HR chatbot can answer questions about:
    - Work hours & flexible arrangements
    - Paid Time Off (PTO) policies
    - Code of conduct
    - Company policies
    
    **Note:** Only answers based on the provided policy document.
    """)
    
    example_questions = [
        "How many PTO days can I get?",
        "What are the standard work hours?",
        "How do I request flexible hours?"
    ]

    for question in example_questions:
        if st.button(question, key=question):
            st.session_state.auto_question = question
            st.rerun()

    # Clear chat button
    if st.button("Clear Chat", type="secondary"):
        st.session_state.messages = []
        st.session_state.chat_session = model.start_chat(history=[])
        st.session_state.auto_question = ""
        st.rerun()
