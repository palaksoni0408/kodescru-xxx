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

def get_snippets(language, topic):
    # Generate 50 snippets related to the topic
    prompt = ChatPromptTemplate.from_template(
        "Generate {count} useful code snippets in {language} related to {topic}. "
        "Provide each snippet with a brief description."
    )
    chain = prompt | llm
    response = chain.invoke({"count": 50, "language": language, "topic": topic})
    return response


def get_projects(level, topic):
    prompt = ChatPromptTemplate.from_template(
        "Generate a list of 10 innovative project ideas related to {topic} suitable for {level} learners. "
        "Provide a brief description for each."
    )
    chain = prompt | llm
    return chain.invoke({"topic": topic, "level": level})

def get_roadmaps(level, topic):
    prompt = ChatPromptTemplate.from_template(
        "Create a detailed learning roadmap for {topic} tailored for {level} learners. "
        "Include key topics and suggested resources for each stage."
    )
    chain = prompt | llm
    return chain.invoke({"topic": topic, "level": level})

def trace_code(code, language):
    prompt = ChatPromptTemplate.from_template(
        "Analyze the following {language} code and provide a step-by-step explanation of its execution flow, "
        "highlighting key variables and decision points:\n\n{code}"
    )
    chain = prompt | llm
    return chain.invoke({"code": code, "language": language})
