import os
from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from euriai import EuriaiLangChainLLM

load_dotenv()

llm = EuriaiLangChainLLM(
    api_key=os.getenv("EURIAI_API_KEY"),
    model="gpt-4.1-nano",
    temperature=0.7,
    max_tokens=300
)

def explain_code(language, topic, level):
    prompt = ChatPromptTemplate.from_template(
        "You are a helpful AI tutor.\nExplain the {topic} in {language} for a {level} learner."
    )
    chain = prompt | llm
    return chain.invoke({"topic": topic, "language": language, "level": level})

def debug_code(language, topic):
    prompt = ChatPromptTemplate.from_template(
        "You are a code reviewer. Find and explain bugs in the following {language} code related to {topic}:\n{code}"
    )
    chain = prompt | llm
    return chain.invoke({"language": language, "topic": topic})

def generate_code(language, topic, level):
    prompt = ChatPromptTemplate.from_template(
        "You are a coding assistant. Generate a {level} level example in {language} on the topic '{topic}'. Include comments."
    )
    chain = prompt | llm
    return chain.invoke({"topic": topic, "language": language, "level": level})

def convert_logic_to_code(logic, language):
    prompt = ChatPromptTemplate.from_template(
        "Convert the following logic or pseudo-code to {language}:\n{logic}"
    )
    chain = prompt | llm
    return chain.invoke({"logic": logic, "language": language})

def analyze_complexity(code):
    prompt = ChatPromptTemplate.from_template(
        "Analyze the time and space complexity of the following code:\n{code}"
    )
    chain = prompt | llm
    return chain.invoke({"code": code})

def trace_code(code, language):
    # Placeholder: Implement real code tracing or use an API
    return "Step-by-step code trace is under development."

def get_snippets(language, snippet_name):
    # Placeholder: Fetch snippets from a database or static data
    snippets_db = {
        "Python": {
            "Hello World": "print('Hello, World!')",
            "Factorial": "def factorial(n): return 1 if n==0 else n*factorial(n-1)"
        },
        "JavaScript": {
            "Alert": "alert('Hello!');",
            "Fetch": "fetch('https://api.example.com')"
        }
    }
    return snippets_db.get(language, {}).get(snippet_name, "Snippet not found.")

def get_projects(level, topic):
    return f"Build a {topic} app suitable for {level} level learners."

def get_roadmaps(level, topic):
    return f"Roadmap for {topic} at {level} level:\n1. Basics\n2. Intermediate\n3. Advanced"
