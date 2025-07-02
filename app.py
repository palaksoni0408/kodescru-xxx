import streamlit as st
import requests
import base64

# Load and encode logo
logo_path = r"C:\Users\palak\OneDrive\Desktop\coding assistant\logo.jpg"
with open(logo_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Custom CSS for responsiveness and styling
st.markdown("""
<style>
/* Responsive layout */
@media(max-width: 768px){
    .header { flex-direction: column; align-items: center; }
    .sidebar { display: none; }
    .content { margin-left: 0; padding: 10px; }
}
.header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    padding: 10px;
    background-color: #f8f9fa;
}
.header img {
    max-width: 120px;
    margin: 10px;
}
.header h1 {
    font-size: 2.5em;
    margin: 10px;
    color: #4CAF50;
}
</style>
""", unsafe_allow_html=True)

# Header with logo and title
st.markdown(f"""
<div class="header">
    <img src='data:image/jpeg;base64,{encoded_string}' />
    <h1>KodesCRUxxx</h1>
</div>
<p style='text-align:center; font-size:1.2em; font-weight:600;'>Your AI-powered Coding Companion for Learning & Building</p>
""", unsafe_allow_html=True)


# Sidebar navigation
st.sidebar.title("Navigation")
menu_option = st.sidebar.radio("Go to", [
    "Home",
    "Explain Code",
    "Debug Code",
    "Generate Code",
    "Convert Logic",
    "Complexity Analysis",
    "Code Tracer",
    "Snippets Library",
    "Project Ideas",
    "Learning Roadmap"
])

API_URL = "http://127.0.0.1:8000"

def fetch_response(endpoint, payload):
    try:
        r = requests.post(f"{API_URL}/{endpoint}", json=payload)
        data = r.json()
        if "response" in data:
            return data["response"]
        else:
            st.error("⚠️ Unexpected API response")
    except Exception as e:
        st.error(f"🚨 API request failed: {e}")

# User inputs
language = st.selectbox("Select Language", ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"])
topic = st.text_input("Enter Topic / Logic / Question")
level = st.selectbox("Select Level", ["Beginner", "Intermediate", "Advanced"])
code_input = st.text_area("Paste your code here", height=200)

# Main content based on selection
if menu_option == "Home":
    st.title("Welcome to KodesCRUxxx!")
    st.write("Use the sidebar to explore features.")

elif menu_option == "Explain Code":
    if st.button("Explain Code", key="explain"):
        with st.spinner("Generating explanation..."):
            resp = fetch_response("explain", {"language": language, "topic": topic, "level": level})
            if resp:
                st.markdown("### 📖 Explanation")
                st.write(resp)

elif menu_option == "Debug Code":
    if st.button("Debug Code", key="debug"):
        with st.spinner("Debugging code..."):
            resp = fetch_response("debug", {"language": language, "topic": topic})
            if resp:
                st.markdown("### 🛠 Debugging")
                st.write(resp)

elif menu_option == "Generate Code":
    if st.button("Generate Code", key="generate"):
        with st.spinner("Generating code..."):
            resp = fetch_response("generate", {"language": language, "topic": topic, "level": level})
            if resp:
                st.markdown("### 💡 Code Example")
                st.code(resp, language=language.lower())

elif menu_option == "Convert Logic":
    logic_input = st.text_area("Enter your logic or pseudo-code")
    target_lang = st.selectbox("Target Language", ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"])
    if st.button("Convert to Code", key="convert"):
        with st.spinner("Converting logic to code..."):
            resp = fetch_response("convert_logic", {"logic": logic_input, "language": target_lang})
            if resp:
                st.markdown("### Converted Code")
                st.code(resp, language=target_lang.lower())

elif menu_option == "Complexity Analysis":
    algo_input = st.text_area("Describe your algorithm or paste code")
    if st.button("Analyze Complexity", key="complexity"):
        with st.spinner("Analyzing complexity..."):
            resp = fetch_response("analyze_complexity", {"code": algo_input})
            if resp:
                st.markdown("### Time & Space Complexity")
                st.write(resp)

elif menu_option == "Code Tracer":
    tracer_input = st.text_area("Paste your code for tracing")
    if st.button("Trace Code", key="trace"):
        with st.spinner("Tracing code..."):
            resp = fetch_response("trace_code", {"code": tracer_input, "language": language})
            if resp:
                st.markdown("### Code Trace")
                st.write(resp)

elif menu_option == "Snippets Library":
    snippets = {
        "Python": ["Hello World", "Factorial"],
        "JavaScript": ["Alert", "Fetch"]
    }
    selected_snippet = st.selectbox("Select Snippet", snippets.get(language, []))
    if st.button("Get Snippet", key="snippet"):
        resp = fetch_response("get_snippets", {"language": language, "snippet": selected_snippet})
        if resp:
            st.code(resp, language=language.lower())

elif menu_option == "Project Ideas":
    if st.button("Get Project Ideas", key="projects"):
        with st.spinner("Fetching project ideas..."):
            resp = fetch_response("get_projects", {"level": level, "topic": topic})
            if resp:
                st.markdown("### Project Ideas")
                st.write(resp)

elif menu_option == "Learning Roadmap":
    if st.button("Get Roadmap", key="roadmap"):
        with st.spinner("Generating roadmap..."):
            resp = fetch_response("get_roadmaps", {"level": level, "topic": topic})
            if resp:
                st.markdown("### Learning Roadmap")
                st.write(resp)

# End of content
st.markdown('&lt;/div>', unsafe_allow_html=True)
