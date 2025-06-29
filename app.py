import streamlit as st
import requests
import base64

# Load and encode logo
logo_path = r"C:\Users\palak\OneDrive\Desktop\coding assistant\logo.jpg"
with open(logo_path, "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Embed CSS for responsiveness
st.markdown("""
<style>
/* Reset some default styles */
body {
    font-family: 'Arial', sans-serif;
    margin: 0;
    padding: 0;
    transition: all 0.3s ease;
}

/* Header with logo and title, responsive flex layout */
.header {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    flex-wrap: wrap;
    padding: 10px;
    background-color: #f8f9fa;
}
.header img {
    max-width: 120px;
    width: 20%;
    height: auto;
    margin: 10px;
}
.header h1 {
    font-size: 2em;
    margin: 10px;
    color: #4CAF50;
}
.header p {
    font-size: 1.2em;
    margin: 10px;
}

/* Sidebar styles for larger screens, hidden on small screens */
.sidebar {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
    width: 220px;
    background-color: #111;
    padding-top: 20px;
    overflow-y: auto;
    transition: all 0.3s ease;
    z-index: 999;
}
.sidebar a {
    display: block;
    padding: 12px 20px;
    color: #ddd;
    text-decoration: none;
    font-size: 1em;
}
.sidebar a:hover {
    background-color: #575757;
    color: #fff;
}

/* Content area with margin to avoid overlap, responsive */
.content {
    margin-left: 240px;
    padding: 20px;
    transition: margin-left 0.3s ease;
}
@media(max-width: 768px){
    /* Stack header vertically on small screens */
    .header {
        flex-direction: column;
        align-items: center;
    }
    /* Hide sidebar, show as top menu or toggle button if needed */
    .sidebar {
        position: relative;
        width: 100%;
        height: auto;
        display: none; /* or block for a toggle menu */
    }
    /* Remove left margin on small screens */
    .content {
        margin-left: 0;
        padding: 10px;
    }
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
    "Learning Roadmap",
    "Motivation & Goals",
    "Collaborative Room",
    "Progress Dashboard",
    "Resume Builder",
    "Tutorials & Repos",
    "Dark Mode"
])

# Main content area
st.markdown('&lt;div class="content">', unsafe_allow_html=True)

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

# Handle menu options
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
    st.subheader("Convert Logic / Pseudo-code to Code")
    logic_input = st.text_area("Enter your logic or pseudo-code")
    target_lang = st.selectbox("Target Language", ["Python", "JavaScript", "Java", "C++", "Ruby", "Go"])
    if st.button("Convert to Code", key="convert_logic"):
        with st.spinner("Converting logic to code..."):
            resp = fetch_response("convert_logic", {"logic": logic_input, "language": target_lang})
            if resp:
                st.markdown("### Converted Code")
                st.code(resp, language=target_lang.lower())

elif menu_option == "Complexity Analysis":
    st.subheader("Algorithm Complexity Analysis")
    algo_input = st.text_area("Describe your algorithm or paste code")
    if st.button("Analyze Complexity", key="complexity"):
        with st.spinner("Analyzing complexity..."):
            resp = fetch_response("analyze_complexity", {"code": algo_input})
            if resp:
                st.markdown("### Time & Space Complexity")
                st.write(resp)

elif menu_option == "Code Tracer":
    st.subheader("Step-by-step Code Tracer")
    tracer_input = st.text_area("Paste your code for tracing")
    if st.button("Trace Code", key="trace"):
        with st.spinner("Tracing code..."):
            resp = fetch_response("trace_code", {"code": tracer_input, "language": language})
            if resp:
                st.markdown("### Code Trace")
                st.write(resp)

elif menu_option == "Snippets Library":
    st.subheader("Code Snippets Library")
    snippets = {
        "Python": ["Hello World", "Factorial Function"],
        "JavaScript": ["Alert Box", "Fetch API Example"]
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

elif menu_option == "Motivation & Goals":
    st.subheader("Set Your Goals & Get Motivated")
    goals = st.text_area("Your Goals / Motivation")
    if st.button("Set Goals", key="goals"):
        st.success("Goals saved! Keep pushing forward!")

elif menu_option == "Collaborative Room":
    st.subheader("Collaborative Coding Room")
    room_id = st.text_input("Room ID")
    if st.button("Join Room", key="join_room"):
        st.info("Joining room... (feature under development)")

elif menu_option == "Progress Dashboard":
    st.subheader("Your Skill Progress")
    st.line_chart([1, 2, 3, 4, 5])

elif menu_option == "Resume Builder":
    st.subheader("Create Your Coding Resume")
    name = st.text_input("Name")
    skills = st.text_area("Skills & Projects")
    if st.button("Build Resume", key="resume"):
        st.success("Resume generated! (feature under development)")

elif menu_option == "Tutorials & Repos":
    st.subheader("Recommended Tutorials & GitHub Repos")
    st.write("[YouTube Tutorials](https://youtube.com)")
    st.write("[GitHub Repos](https://github.com)")

# End of content
st.markdown('&lt;/div>', unsafe_allow_html=True)
