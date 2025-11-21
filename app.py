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

st.title("Onboarding HR Assistant")

# Custom CSS for full-page background and transparent main content
st.markdown("""
<style>
    .stApp {
        background-color: transparent;
    }
    #firefly-canvas {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
    }

    [data-testid="stChatMessage"] {
        padding: 10px 15px;
        border-radius: 20px;
        margin-bottom: 10px;
        max-width: 75%;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        display: flex;
        align-items: flex-start;
        gap: 10px;
    }

    /* Assistant messages (bot) */
    [data-testid="stChatMessage"]:nth-child(even) {
        background-color: rgba(47, 79, 47, 0.8) !important; /* Swampy green */
        color: white !important;
        margin-right: auto;
        flex-direction: row;
    }

    /* User messages */
    [data-testid="stChatMessage"]:nth-child(odd) {
        background-color: rgba(100, 149, 237, 0.8) !important; /* Cornflower blue */
        color: white !important;
        margin-left: auto;
        flex-direction: row-reverse;
    }

    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        color: inherit !important;
    }

    [data-testid="stChatMessage"] p {
        color: inherit !important;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(to right, #000000, #434343);
        color: white;
    }
    [data-testid="stSidebar"] h3 {
        color: #FFD700;
    }
    [data-testid="stSidebar"] .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 12px;
        width: 100%;
    }
    [data-testid="stSidebar"] .stButton>button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# Add the firefly animation
st.markdown("""
<canvas id="firefly-canvas"></canvas>
<script>
    const canvas = document.getElementById('firefly-canvas');
    const ctx = canvas.getContext('2d');

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    const fireflies = [];
    const numFireflies = 50;

    class Firefly {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.radius = Math.random() * 2 + 1;
            this.speedX = (Math.random() - 0.5) * 0.5;
            this.speedY = (Math.random() - 0.5) * 0.5;
            this.opacity = Math.random() * 0.5 + 0.5;
        }

        update() {
            this.x += this.speedX;
            this.y += this.speedY;

            if (this.x < 0 || this.x > canvas.width) {
                this.speedX *= -1;
            }

            if (this.y < 0 || this.y > canvas.height) {
                this.speedY *= -1;
            }
        }

        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(255, 255, 0, ${this.opacity})`;
            ctx.fill();
        }
    }

    function init() {
        for (let i = 0; i < numFireflies; i++) {
            fireflies.push(new Firefly());
        }
    }

    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (const firefly of fireflies) {
            firefly.update();
            firefly.draw();
        }

        requestAnimationFrame(animate);
    }

    init();
    animate();

    window.addEventListener('resize', () => {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
</script>
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
        st.markdown(message["content"])

user_input = st.chat_input("Enter your question here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(user_input)

    with st.chat_message("assistant", avatar="🤖"):
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

# Add example questions
example_questions = [
    "How many PTO days can I get?",
    "What are the standard work hours?",
    "How do I request flexible hours?"
]

# what chatbot can answer limit
with st.sidebar:
    st.markdown("""
        <style>
            [data-testid="stSidebar"] {
                background: linear-gradient(to right, #000000, #434343);
                color: white;
            }
            [data-testid="stSidebar"] h3 {
                color: #FFD700;
            }
            [data-testid="stSidebar"] .stButton>button {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 24px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
                border-radius: 12px;
                width: 100%;
            }
            [data-testid="stSidebar"] .stButton>button:hover {
                background-color: white;
                color: black;
                border: 2px solid #4CAF50;
            }
        </style>
    """, unsafe_allow_html=True)
    
    st.subheader("Example Questions")
    
    st.markdown("""
    This HR chatbot can answer questions about:
    - Work hours & flexible arrangements
    - Paid Time Off (PTO) policies
    - Code of conduct
    - Company policies
    
    **Note:** Only answers based on the provided policy document.
    """)
    for question in example_questions:
        if st.button(question, key=question):
            st.session_state.auto_question = question
            st.rerun()

if "auto_question" in st.session_state and st.session_state.auto_question:
    user_input = st.session_state.auto_question
    st.session_state.auto_question = ""  # Reset after use
else:
    user_input = st.chat_input("Ask about company policy...")


# Clear chat button
if st.sidebar.button("Clear Chat", type="secondary"):
    st.session_state.messages = []
    st.session_state.chat_session = model.start_chat(history=[])
    st.session_state.auto_question = ""
    st.rerun()

