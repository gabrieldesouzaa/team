import streamlit as st
import google.generativeai as genai
import os

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
Do not use any external knowledge or make assumptions. 
If a question cannot be answered from the policy, state that the information is not available in the policy document and do not apologize. 
Keep your answers concise, clear, and professional. Format your answers using markdown for better readability where appropriate (e.g., lists, bold text).

Here is the company policy:
---
{COMPANY_POLICY}
---
"""

# Streamlit UI
st.title("Innovate Inc. HR Chatbot")

if "chat_session" not in st.session_state:
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        system_instruction=SYSTEM_INSTRUCTION
    )
    st.session_state.chat_session = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Enter your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = st.session_state.chat_session.send_message(user_input)
                assistant_response = response.text
                st.markdown(assistant_response)
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})
            except Exception as e:
                st.error(f"An error occurred: {e}")
                st.session_state.messages.append({"role": "assistant", "content": f"Error: {e}"})

# Add history management to prevent infinite growth
MAX_HISTORY = 50  # keep last 50 messages

if len(st.session_state.messages) > MAX_HISTORY:
    st.session_state.messages = st.session_state.messages[-MAX_HISTORY:]

def validate_input(user_input):
    """Basic input validation"""
    if not user_input or user_input.strip() == "":
        return False, "Type your question here."
    if len(user_input) > 1000:
        return False, "Question too long. Please keep under 1000 characters."
    return True, ""

# main logic:
if user_input:
    is_valid, validation_msg = validate_input(user_input)
    if not is_valid:
        st.warning(validation_msg)
    else:


# what chatbot can answer limit
with st.sidebar:
    st.header("About")
    st.markdown("""
    This HR chatbot can answer questions about:
    - Work hours & flexible arrangements
    - Paid Time Off (PTO) policies
    - Code of conduct
    - Company policies
    
    **Note:** Only answers based on the provided policy document.
    """)

# Add a clear conversation button
col1, col2 = st.columns([3, 1])
with col2:
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.session_state.chat_session = model.start_chat(history=[])
        st.rerun()

# Add example questions
st.sidebar.subheader("Example Questions")
example_questions = [
    "How many PTO days do I get?",
    "What are the standard work hours?",
    "How do I request flexible hours?"
]

for q in example_questions:
    if st.sidebar.button(q, key=q):
        # This would trigger the chat input
        st.session_state.auto_question = q