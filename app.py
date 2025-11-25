import streamlit as st
import os
try:
    from dotenv import load_dotenv
except Exception:
    # Provide a conservative fallback so the app doesn't crash at import time
    # If dotenv isn't installed, load_dotenv becomes a no-op and the app can
    # still run if environment variables are provided by the environment.
    def load_dotenv():
        return False
try:
    from google.generativeai.types import HarmCategory, HarmBlockThreshold
    import google.generativeai as genai
except Exception as e:
    # Provide a clear, actionable error so the user can install the required package.
    raise RuntimeError(
        "Missing required package 'google-generativeai'.\n"
        "Install it with: `pip install google-generativeai` or `pip install -r requirements.txt`.\n"
        f"Original import error: {e}"
    )
from handbook import HANDBOOK_TEXT, COMPANY_NAME, DENY_MESSAGE, load_handbook_file
import json
import hashlib
import secrets as _secrets
from typing import Optional
import re
from collections import Counter

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

# Allow overriding the bundled handbook via the `HANDBOOK_PATH` environment variable.
_handbook_path = os.environ.get("HANDBOOK_PATH")
if _handbook_path:
    try:
        HANDBOOK_TEXT = load_handbook_file(_handbook_path)
    except Exception as e:
        raise RuntimeError(f"Failed to load handbook from { _handbook_path }: {e}")
MODEL_ID = "gemini-2.5-flash"

# --- System Prompt ---
def get_system_prompt(question: str = "", user_state: str = ""):
    """Generate system prompt with relevant handbook sections based on the question."""
    if question:
        handbook_excerpt = extract_relevant_sections(question, HANDBOOK_TEXT, max_chars=10000, user_state=user_state)
    else:
        # Fallback if no question provided
        handbook_excerpt = HANDBOOK_TEXT[:10000] + ("\n... [truncated] ..." if len(HANDBOOK_TEXT) > 10000 else "")
    
    return f"""
You are an HR onboarding assistant for {COMPANY_NAME}. Your scope is to answer questions about new employee onboarding, official company policies (see handbook below), and—if PERSONAL_DATA is provided—answer personal questions about the authenticated user using that data. If asked anything else and no PERSONAL_DATA is provided, you MUST respond with: "{DENY_MESSAGE}"

If PERSONAL_DATA is provided, use it to answer personal/account-specific questions (e.g., PTO, pay rate, employee info) for the authenticated user.

COMPANY HANDBOOK (relevant sections):
---
{handbook_excerpt}
---
""".strip()

# --- Gemini API Configuration ---
# Read and sanitize GEMINI_API_KEY (strip surrounding quotes/newlines)
api_key = os.environ.get("GEMINI_API_KEY", "")
api_key = api_key.strip().strip('"').strip("'")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY environment variable is not set or is empty. Please set it in your .env or environment.")
if len(api_key) < 20:
    raise RuntimeError("GEMINI_API_KEY appears to be malformed or too short. Check your .env formatting.")
try:
    genai.configure(api_key=api_key)
except Exception as e:
    raise RuntimeError(f"Failed to configure Gemini client: {e}")
model = genai.GenerativeModel(MODEL_ID)

# --- Streamlit UI ---
st.set_page_config(layout="centered", page_title=f"{COMPANY_NAME} Onboarding")

# --- Simple local auth helpers (demo only) ---

_USERS_FILE = os.path.join(os.path.dirname(__file__), "users.json")
_PERSONAL_DATA_FILE = os.path.join(os.path.dirname(__file__), "personal_data.json")

def _ensure_file(path: str, initial: dict | list | str = None):
    if not os.path.exists(path):
        with open(path, "w", encoding="utf-8") as f:
            if isinstance(initial, (dict, list)):
                json.dump(initial, f, indent=2)
            elif isinstance(initial, str):
                f.write(initial)
            else:
                f.write("{}")
        try:
            os.chmod(path, 0o600)
        except Exception:
            pass

def _load_json(path: str) -> dict:
    _ensure_file(path, {})
    with open(path, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except Exception:
            return {}

def _save_json(path: str, data: dict):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    try:
        os.chmod(path, 0o600)
    except Exception:
        pass

def _hash_passphrase(passphrase: str, salt: Optional[bytes] = None):
    if salt is None:
        salt = _secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", passphrase.encode("utf-8"), salt, 200_000)
    return salt.hex(), dk.hex()

def create_user(username: str, passphrase: str) -> bool:
    username = username.strip().lower()
    users = _load_json(_USERS_FILE)
    if username in users:
        return False
    salt_hex, hash_hex = _hash_passphrase(passphrase)
    users[username] = {"salt": salt_hex, "hash": hash_hex}
    _save_json(_USERS_FILE, users)
    return True

def verify_user(username: str, passphrase: str) -> bool:
    username = username.strip().lower()
    users = _load_json(_USERS_FILE)
    record = users.get(username)
    if not record:
        return False
    salt = bytes.fromhex(record["salt"])
    _, derived = _hash_passphrase(passphrase, salt=salt)
    return _secrets.compare_digest(derived, record["hash"])

def load_personal_data() -> dict:
    return _load_json(_PERSONAL_DATA_FILE)

def save_personal_data(data: dict):
    _save_json(_PERSONAL_DATA_FILE, data)

def needs_authentication(question: str) -> bool:
    """Heuristic: return True if the user is asking for personal/account-specific info.

    This is intentionally conservative: it looks for first-person pronouns and
    common personal/account keywords.
    """
    if not question:
        return False
    q = question.lower()
    personal_triggers = [" my ", "my ", " me ", "mine", "myself", "on file", "on record", "account", "payroll", "payout", "balance", "pay stub", "email on file", "phone on file", "what is my", "show me my", "do i have", "am i", "my pto", "my balance"]
    for t in personal_triggers:
        if t in q:
            return True
    return False


def _tokenize(text: str):
    """Simple word tokenizer for relevance scoring."""
    return re.findall(r"\w+", text.lower())


def extract_relevant_sections(question: str, handbook_text: str, max_chars: int = 10000, user_state: str = "") -> str:
    """Extract the most relevant handbook sections for the given question.
    
    Splits handbook by paragraphs, scores each by keyword overlap with the question,
    and returns top sections up to max_chars. If user_state is provided, boosts
    sections that mention that state.
    """
    if not handbook_text or not question:
        return handbook_text[:max_chars] if handbook_text else ""
    
    # Split into sections by double newlines (paragraphs)
    sections = [s.strip() for s in re.split(r"\n{2,}", handbook_text) if s.strip()]
    if not sections:
        return handbook_text[:max_chars]
    
    # Tokenize question
    q_tokens = set(_tokenize(question))
    if not q_tokens:
        return handbook_text[:max_chars]
    
    # Score each section by keyword overlap
    scored = []
    for section in sections:
        s_tokens = _tokenize(section)
        if not s_tokens:
            continue
        # Count overlapping keywords
        overlap = sum(Counter(s_tokens)[t] for t in q_tokens)
        
        # Boost score if user's state is mentioned in this section
        state_boost = 0
        if user_state:
            if user_state.lower() in section.lower():
                state_boost = 10  # Strong boost for state match
        
        final_score = overlap + state_boost
        scored.append((final_score, section))
    
    if not scored:
        return handbook_text[:max_chars]
    
    # Sort by relevance (highest first) and concatenate top sections
    scored.sort(key=lambda x: x[0], reverse=True)
    result_parts = []
    total_len = 0
    
    for score, section in scored:
        if score == 0 and result_parts:
            # Stop if we have some results and next sections aren't relevant
            break
        piece = section + "\n\n"
        if total_len + len(piece) > max_chars:
            # Add partial section if space remains
            remain = max_chars - total_len
            if remain > 100:
                result_parts.append(piece[:remain])
            break
        result_parts.append(piece)
        total_len += len(piece)
    
    result = "".join(result_parts).strip()
    return result if result else handbook_text[:max_chars]


def _extract_response_text(response) -> str:
    """Robustly extract text from a Gemini `generate_content` response.

    The SDK can return different shapes depending on model, safety blocks,
    or partial results. Try a few common access patterns and fall back to
    a helpful error message.
    """
    try:
        # Preferred quick accessor
        if hasattr(response, "text") and response.text:
            return response.text
    except Exception:
        pass
    try:
        # Try a common candidate-based structure
        candidates = getattr(response, "candidates", None)
        if candidates and len(candidates) > 0:
            cand = candidates[0]
            # Some SDK versions put text on candidate.text
            if hasattr(cand, "text") and cand.text:
                return cand.text
            # Or nested content parts: cand.content[0].text
            parts = getattr(cand, "content", None)
            if parts and len(parts) > 0:
                first = parts[0]
                txt = getattr(first, "text", None) or getattr(first, "content", None)
                if isinstance(txt, str) and txt:
                    return txt
    except Exception:
        pass
    try:
        # Last-resort: try stringifying the whole response (safe fallback)
        return str(response)
    except Exception:
        return "(no assistant text returned)"

# Create a test account automatically if none exists so you can verify quickly.
# Test credentials:
#   username: testuser
#   passphrase: TestPass123!
TEST_USERNAME = "testuser"
TEST_PASSPHRASE = "TestPass123!"
users = _load_json(_USERS_FILE)
if TEST_USERNAME not in users:
    create_user(TEST_USERNAME, TEST_PASSPHRASE)
    pdata = load_personal_data()
    pdata.setdefault(TEST_USERNAME, {
        "email": "testuser@example.com",
        "phone": "555-0100",
        "state": "Ohio",
        "home_address": "123 Main St, Columbus, OH",
        "pay_rate": "15.00",
        "hours_pto": 40,
        "hours_sick_time": 40,
        "employee_number": "1001",
        "job_title": "Sales Associate",
        "disability": "None",
    })
    save_personal_data(pdata)

# Initialize Session state for auth
if "auth_user" not in st.session_state:
    st.session_state.auth_user = None
    st.session_state.auth_ok = False
    st.session_state.login_attempts = 0
    st.session_state.pending_protected_question = None
    st.session_state._expecting_login = False

# Custom HTML Structure
st.markdown("""
<div class="app-container">
    <header class="app-header">
        <h1>Onboarding Assistant</h1>
        <p>Ask about new-hire onboarding and company policies</p>
    </header>
""", unsafe_allow_html=True)

# Chat-driven authentication: no sidebar login. Authentication is triggered
# only when the user asks for personal information (see `needs_authentication`).

# Initialize Chat History
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

# Chat Input (chat-driven auth)
if prompt := st.chat_input("Ask about company policies..."):
    # Add user message to display
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Handle chat commands: /edit, /login and /logout
    low = prompt.strip()
    processed = False
    if low.lower().startswith("/edit"):
        # Open the personal info edit form in main area if authenticated
        if st.session_state.get("auth_ok") and st.session_state.get("auth_user"):
            st.session_state._edit_personal = True
            reply = "Opening personal info editor for your account."
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        else:
            st.session_state.pending_protected_question = None
            reply = "You must authenticate first. Please type `/login username passphrase`."
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        processed = True
    if low.lower().startswith("/login "):
        # expected format: /login <username> <passphrase>
        parts = prompt.strip().split(maxsplit=2)
        if len(parts) < 3:
            reply = "Please provide credentials in the format: `/login username passphrase`"
            st.session_state.messages.append({"role": "assistant", "content": reply})
        else:
            username = parts[1].strip()
            passphrase = parts[2]
            if verify_user(username, passphrase):
                st.session_state.auth_user = username.strip().lower()
                st.session_state.auth_ok = True
                st.session_state.login_attempts = 0
                reply = f"Authenticated as {username}."
                st.session_state.messages.append({"role": "assistant", "content": reply})
                with st.chat_message("assistant"):
                    st.markdown(reply)
                # If there was a pending protected question, answer it now
                pq = st.session_state.get("pending_protected_question")
                if pq:
                    st.session_state.pending_protected_question = None
                    # generate answer including personal data
                    personal = load_personal_data()
                    me = personal.get(st.session_state.auth_user, {})
                    user_state = me.get("state", "")
                    api_history = [
                        {"role": "user", "parts": [get_system_prompt(pq, user_state)]},
                        {"role": "user", "parts": [f"PERSONAL_DATA: {json.dumps(me)}"]},
                        {"role": "user", "parts": [pq]},
                    ]
                    with st.chat_message("assistant"):
                        message_placeholder = st.empty()
                        try:
                            response = model.generate_content(
                                api_history,
                                generation_config={"temperature": 0.4, "max_output_tokens": 2048},
                            )
                            full_response = _extract_response_text(response)
                            message_placeholder.markdown(full_response)
                        except Exception as e:
                            st.error(f"An error occurred: {e}")
                            full_response = "Sorry, I ran into an error. Please try again."
                            message_placeholder.markdown(full_response)
                    st.session_state.messages.append({"role": "assistant", "content": full_response})
            else:
                st.session_state.login_attempts = st.session_state.get("login_attempts", 0) + 1
                reply = "Invalid credentials."
                st.session_state.messages.append({"role": "assistant", "content": reply})
                with st.chat_message("assistant"):
                    st.markdown(reply)
        processed = True
    elif low.lower().strip() == "/logout":
        st.session_state.auth_user = None
        st.session_state.auth_ok = False
        reply = "Logged out."
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
        processed = True

    # If no command consumed the prompt, continue normal handling
    if not processed:
        # If the question requests personal info and user is not authenticated, prompt for login
        if needs_authentication(prompt) and not st.session_state.get("auth_ok"):
            st.session_state.pending_protected_question = prompt
            login_prompt = (
                "To answer that I need to access your personal information. "
                "Please authenticate by typing `/login username passphrase` in the chat."
            )
            st.session_state.messages.append({"role": "assistant", "content": login_prompt})
            with st.chat_message("assistant"):
                st.markdown(login_prompt)
            processed = True
        else:
            # Build api_history; include personal data if authenticated and the question is personal
            user_state = ""
            if st.session_state.get("auth_ok"):
                personal = load_personal_data()
                me = personal.get(st.session_state.auth_user, {})
                user_state = me.get("state", "")
            
            api_history = [
                {"role": "user", "parts": [get_system_prompt(prompt, user_state)]}
            ]
            if st.session_state.get("auth_ok") and needs_authentication(prompt):
                api_history.append({"role": "user", "parts": [f"PERSONAL_DATA: {json.dumps(me)}"]})

            # Only include the last 4 chat messages to avoid token overflow
            recent_msgs = st.session_state.messages[-4:] if len(st.session_state.messages) > 4 else st.session_state.messages
            api_history += [
                {"role": "user" if msg["role"] == "user" else "model", "parts": [msg["content"]]}
                for msg in recent_msgs
            ]

            # Get response from Gemini
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                try:
                    response = model.generate_content(
                        api_history,
                        generation_config={
                            "temperature": 0.4,
                            "max_output_tokens": 2048,
                        },
                        safety_settings={
                            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
                            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
                            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
                            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
                        },
                    )
                    full_response = _extract_response_text(response)
                    message_placeholder.markdown(full_response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                    full_response = "Sorry, I ran into an error. Please try again."
                    message_placeholder.markdown(full_response)
            
            # Add assistant response to display history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

# Close the main app div
st.markdown('</div>', unsafe_allow_html=True)
