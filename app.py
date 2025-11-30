import streamlit as st
import os
# Version marker
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
You are an HR onboarding assistant for {COMPANY_NAME}. 

YOU ARE AUTHORIZED AND EXPECTED TO ANSWER:
1. New employee onboarding and orientation questions
2. Company policies, procedures, and guidelines from the handbook
3. Employee benefits (PTO, sick leave, insurance, 401k, discounts, perks, accruals)
4. Work schedules, shifts, time tracking, and leave policies
5. Compensation, pay rates, payroll, and salary information
6. Company culture, values, workplace conduct, and dress code
7. Personal/account-specific information when PERSONAL_DATA is provided

IMPORTANT PERMISSION RULES:
- You HAVE PERMISSION to answer ALL work-related questions from the handbook
- You HAVE PERMISSION to discuss benefits, discounts, PTO, pay, schedules, and policies
- When PERSONAL_DATA is provided, you MUST answer personal questions using that data
- ONLY refuse questions about non-work topics (weather, news, sports, general knowledge)
- If a question relates to employment, benefits, or company policies, YOU SHOULD ANSWER IT

USING PERSONAL_DATA:
- When PERSONAL_DATA is provided, it contains the user's "state" field
- Use the state to determine which PTO Model applies (check the state/PTO model chart in the handbook)
- For questions like "what PTO model applies to me?" or "how much PTO do I get?", you MUST:
  1. Look at the "state" field in PERSONAL_DATA
  2. Find that state in the handbook's state/PTO model chart
  3. Identify which Model (1-5) applies
  4. Provide the specific PTO accrual details for that model
- Example: If PERSONAL_DATA shows "state": "California", you should explain that California follows Model 4 and provide Model 4 PTO details

SECURITY RULES:
- ONLY provide personal data (specific PTO balance, pay rate, employee number) for the AUTHENTICATED user
- NEVER provide another employee's personal information (their specific PTO hours, pay rate, employee number, etc.)
- When asked about another employee's benefits/policies (discount, general PTO policy), explain that all employees follow the same company policies and answer with the general policy
- Example: "What's Bob's discount?" → "All employees receive the same 40% discount on regular-priced merchandise"
- General policy questions do NOT require authentication
- Personal questions ("my PTO", "my pay rate") require PERSONAL_DATA

RESPONSE STYLE:
- Keep responses BRIEF and CONCISE (2-4 sentences typically)
- Provide direct answers with key facts and numbers
- Only quote handbook verbatim if user asks for "exact wording", "quote", or "citation"
- Use conversational, clear language
- Always include specific numbers when discussing percentages, amounts, hours, or days

For non-work topics (weather, news, entertainment), respond with: "{DENY_MESSAGE}"

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

    Recognizes first-person pronouns, possessives, and common personal/work-related keywords.
    """
    if not question:
        return False
    q = question.lower()
    
    # Self-referential words and pronouns
    personal_triggers = [
        " my ", "my ", " me ", " i ", "mine", "myself", " i'm ", " i am ",
        "do i ", "am i ", "can i ", "will i ", "should i ", "have i ",
        "what's my", "what is my", "show me my", "tell me my", "get my",
        "where is my", "when is my", "how much is my", "how many"
    ]
    
    # Personal data and work-related keywords that need authentication
    work_triggers = [
        "pto", "vacation", "sick time", "sick leave", "sick day",
        "pay rate", "salary", "wage", "payroll", "paycheck", "pay stub",
        "employee number", "employee id", "job title", "position",
        "benefits", "insurance", "coverage", "401k", "retirement",
        "email on file", "phone on file", "address on file", "on record",
        "balance", "accrual", "hours", "days off", "time off",
        "state", "location", "home address", "contact info",
        "disability", "accommodation", "schedule", "shift"
    ]
    
    # Check for personal triggers - these almost always need auth
    for t in personal_triggers:
        if t in q:
            return True
    
    # For work triggers, only require auth if combined with personal context
    # This allows general questions about discounts/benefits without auth
    for t in work_triggers:
        if t in q:
            # Check if it's asking about "my" or personal info
            if any(p in q for p in [" my ", " i ", " me ", "mine"]):
                return True
    
    return False


def is_asking_about_other_employee(question: str) -> tuple[bool, str]:
    """Detect if question is about another specific employee.
    
    Returns (True, employee_name) if asking about someone else, (False, "") otherwise.
    """
    if not question:
        return False, ""
    
    q = question.lower()
    
    # Common employee names to check (can be expanded)
    employee_patterns = [
        (r"\bbob'?s?\b", "bob"),
        (r"\balice'?s?\b", "alice"),
        (r"\bjohn'?s?\b", "john"),
        (r"\bmary'?s?\b", "mary"),
        (r"\bsarah'?s?\b", "sarah"),
    ]
    
    for pattern, name in employee_patterns:
        if re.search(pattern, q):
            return True, name
    
    # Also check for "someone else", "other employee", etc.
    if any(phrase in q for phrase in ["someone else", "other employee", "another employee", "another person"]):
        return True, "another employee"
    
    return False, ""


def _tokenize(text: str):
    """Simple word tokenizer for relevance scoring."""
    return re.findall(r"\w+", text.lower())


def _extract_phrases(text: str):
    """Extract 2-3 word phrases from text for better matching."""
    words = _tokenize(text)
    phrases = []
    # Add single words
    phrases.extend(words)
    # Add 2-word phrases
    for i in range(len(words) - 1):
        phrases.append(f"{words[i]} {words[i+1]}")
    # Add 3-word phrases
    for i in range(len(words) - 2):
        phrases.append(f"{words[i]} {words[i+1]} {words[i+2]}")
    return phrases


def _expand_query(question: str):
    """Expand query with synonyms and related terms for better matching."""
    q = question.lower()
    expansions = set(_tokenize(q))
    
    # Common synonym mappings for HR/benefits terms
    synonyms = {
        "discount": ["discount", "savings", "employee purchase", "price reduction", "associate discount"],
        "pto": ["pto", "paid time off", "vacation", "time off", "leave", "days off"],
        "sick": ["sick", "sick leave", "sick time", "sick day", "illness"],
        "pay": ["pay", "salary", "wage", "compensation", "paycheck", "earnings"],
        "benefit": ["benefit", "benefits", "perks", "coverage", "insurance"],
        "schedule": ["schedule", "shift", "hours", "time", "work hours"],
        "accrual": ["accrual", "accrue", "accrued", "earn", "accumulate"],
        "policy": ["policy", "policies", "rule", "rules", "guideline"],
        "dress code": ["dress code", "attire", "clothing", "uniform", "appearance"],
        "bereavement": ["bereavement", "funeral", "death", "grieving"],
        "401k": ["401k", "retirement", "savings plan", "pension"],
        "model": ["model", "pto", "plan", "category", "tier", "version"],
    }
    
    # Add synonyms for words in the question
    for word, syns in synonyms.items():
        if word in q:
            expansions.update(syns)
    
    return list(expansions)


def extract_relevant_sections(question: str, handbook_text: str, max_chars: int = 10000, user_state: str = "") -> str:
    """Extract the most relevant handbook sections for the given question.
    
    Uses multi-word phrase matching, synonym expansion, and weighted scoring
    to find the best matching sections from the handbook. Keeps related lines
    together to preserve context and numeric details.
    """
    if not handbook_text or not question:
        return handbook_text[:max_chars] if handbook_text else ""
    
    # Split into sections - keep related content together
    sections = []
    
    # First split by double newlines (paragraphs)
    parts = re.split(r"\n{2,}", handbook_text)
    
    for part in parts:
        part = part.strip()
        if not part:
            continue
        
        # Keep sections under 1500 chars together (preserves context)
        if len(part) <= 1500:
            sections.append(part)
        else:
            # For very long sections, split more carefully
            lines = part.split('\n')
            current_chunk = []
            current_len = 0
            
            for line in lines:
                line = line.strip()
                if not line or len(line) < 20:
                    continue
                
                # Keep building chunk if under 800 chars
                if current_len + len(line) < 800:
                    current_chunk.append(line)
                    current_len += len(line)
                else:
                    # Save current chunk and start new one
                    if current_chunk:
                        sections.append('\n'.join(current_chunk))
                    current_chunk = [line]
                    current_len = len(line)
            
            # Add final chunk
            if current_chunk:
                sections.append('\n'.join(current_chunk))
    
    if not sections:
        return handbook_text[:max_chars]
    
    # Get expanded query terms (with synonyms)
    query_terms = _expand_query(question)
    query_phrases = _extract_phrases(question)
    
    # Score each section
    scored = []
    for section in sections:
        section_lower = section.lower()
        section_tokens = _tokenize(section)
        
        if not section_tokens:
            continue
        
        # Calculate multiple relevance signals
        score = 0
        
        # 1. Exact phrase matching (highest weight)
        for phrase in query_phrases:
            if phrase in section_lower:
                # Longer phrases get more weight
                phrase_len = len(phrase.split())
                score += phrase_len * 5
        
        # 2. Individual term frequency (with synonyms)
        term_freq = Counter(section_tokens)
        for term in query_terms:
            if term in section_lower:
                score += term_freq.get(term, 0) * 2
        
        # 3. Term overlap score
        overlap = len(set(query_terms) & set(section_tokens))
        score += overlap
        
        # 4. Boost for state match and state/model chart
        if user_state:
            state_lower = user_state.lower()
            # Strong boost if state name appears
            if state_lower in section_lower:
                score += 20
            # Also boost if this looks like the state/PTO model chart
            if 'pto model' in section_lower and 'state' in section_lower:
                score += 25  # Very high boost for the mapping table
            # If asking about PTO/model and user has a state, boost model sections
            if any(term in question.lower() for term in ['pto', 'model', 'time off', 'vacation']):
                # Boost sections that mention any model number
                if re.search(r'model\s+[1-5]', section_lower):
                    score += 10
        
        # 5. Boost for section headings/titles (ALL CAPS or title-like)
        first_line = section.split('\n')[0] if '\n' in section else section
        if first_line.isupper() or (len(first_line) < 100 and first_line and first_line[0].isupper()):
            # This might be a heading - boost if it matches
            if any(term in first_line.lower() for term in query_terms[:5]):
                score += 5
        
        # 6. Boost sections with numbers/percentages (likely contain specific details)
        if re.search(r'\d+%|\d+\s*percent|\$\d+|\d+\s*hours?|\d+\s*days?', section):
            if score > 0:  # Only boost if already relevant
                score += 2
        
        scored.append((score, section))
    
    if not scored:
        return handbook_text[:max_chars]
    
    # Sort by relevance (highest first)
    scored.sort(key=lambda x: x[0], reverse=True)
    
    # Take top sections up to max_chars
    result_parts = []
    total_len = 0
    seen_content = set()  # Avoid duplicates
    
    for score, section in scored:
        # Skip if score is 0 and we already have results
        if score == 0 and result_parts:
            break
        
        # Skip near-duplicates
        section_sig = section[:100].lower()
        if section_sig in seen_content:
            continue
        seen_content.add(section_sig)
        
        piece = section + "\n\n"
        if total_len + len(piece) > max_chars:
            remain = max_chars - total_len
            if remain > 200:  # Only add if we have meaningful space
                result_parts.append(piece[:remain])
            break
        
        result_parts.append(piece)
        total_len += len(piece)
        
        # Take top 25 sections max
        if len(result_parts) >= 25:
            break
    
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

# Create test accounts automatically if none exists so you can verify quickly.
# Test credentials:
#   username: testuser / passphrase: TestPass123!
#   username: bob / passphrase: BobPass456!
# Personal data for all users is stored in personal_data.json
TEST_USERS = {
    "testuser": "TestPass123!",
    "bob": "BobPass456!"
}

users = _load_json(_USERS_FILE)

for username, passphrase in TEST_USERS.items():
    if username not in users:
        create_user(username, passphrase)

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
                
                # Load and store personal data in session for this user
                personal = load_personal_data()
                me = personal.get(st.session_state.auth_user, {})
                st.session_state.user_personal_data = me
                
                # Provide confirmation with personal data context
                reply = f"Authenticated as {username}. I now have access to your personal information and can answer questions about your specific benefits, PTO, pay rate, and other account details."
                st.session_state.messages.append({"role": "assistant", "content": reply})
                with st.chat_message("assistant"):
                    st.markdown(reply)
                # If there was a pending protected question, answer it now
                pq = st.session_state.get("pending_protected_question")
                if pq:
                    st.session_state.pending_protected_question = None
                    # generate answer including personal data
                    user_state = me.get("state", "")
                    state_info = me.get("state", "Unknown")
                    personal_data_msg = f"""PERSONAL_DATA: {json.dumps(me)}

CRITICAL INSTRUCTION: The user's state is "{state_info}". When answering questions about PTO models, benefits, or policies that vary by location, you MUST:
1. Check the state/PTO model chart in the handbook to find which Model applies to {state_info}
2. Provide the specific details for that Model
3. Do NOT ask the user for their state - you already have it in PERSONAL_DATA above"""
                    api_history = [
                        {"role": "user", "parts": [get_system_prompt(pq, user_state)]},
                        {"role": "user", "parts": [personal_data_msg]},
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
        st.session_state.user_personal_data = None  # Clear personal data
        reply = "Logged out. I no longer have access to your personal information."
        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)
        processed = True

    # If no command consumed the prompt, continue normal handling
    if not processed:
        # Check if asking about another employee's general benefits
        is_other_emp, emp_name = is_asking_about_other_employee(prompt)
        
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
            context_note = ""
            me = {}
            
            if st.session_state.get("auth_ok"):
                # Use session-stored personal data if available, otherwise load fresh
                if "user_personal_data" in st.session_state and st.session_state.user_personal_data:
                    me = st.session_state.user_personal_data
                else:
                    personal = load_personal_data()
                    me = personal.get(st.session_state.auth_user, {})
                    st.session_state.user_personal_data = me
                user_state = me.get("state", "")
            
            # If asking about another employee, add context note
            if is_other_emp:
                context_note = f"\n\nNOTE: User is asking about {emp_name}. You should explain that all employees follow the same company policies and provide the general policy answer. Do NOT provide specific personal data for other employees."
            
            api_history = [
                {"role": "user", "parts": [get_system_prompt(prompt, user_state) + context_note]}
            ]
            # Always include PERSONAL_DATA if user is authenticated, so bot has full context
            if st.session_state.get("auth_ok") and me:
                state_info = me.get("state", "Unknown")
                personal_data_msg = f"""PERSONAL_DATA: {json.dumps(me)}

CRITICAL INSTRUCTION: The user's state is "{state_info}". When answering questions about PTO models, benefits, or policies that vary by location, you MUST:
1. Check the state/PTO model chart in the handbook to find which Model applies to {state_info}
2. Provide the specific details for that Model
3. Do NOT ask the user for their state - you already have it in PERSONAL_DATA above"""
                api_history.append({"role": "user", "parts": [personal_data_msg]})

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
