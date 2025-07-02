from fastapi import FastAPI
from pydantic import BaseModel
from ai_engine import (
    explain_code,
    debug_code,
    generate_code,
    convert_logic_to_code,
    analyze_complexity,
    trace_code,
    get_snippets,
    get_projects,
    get_roadmaps
)

app = FastAPI()

class RequestModel(BaseModel):
    language: str = None
    code: str = None
    topic: str = None
    level: str = None
    logic: str = None
    snippet: str = None
    snippet_name: str = None
    project_topic: str = None
    roadmap_topic: str = None

@app.post("/explain")
def explain(req: RequestModel):
    return {"response": explain_code(req.language, req.topic, req.level)}

@app.post("/debug")
def debug(req: RequestModel):
    return {"response": debug_code(req.language, req.topic)}

@app.post("/generate")
def generate(req: RequestModel):
    return {"response": generate_code(req.language, req.topic, req.level)}

@app.post("/convert_logic")
def convert_logic(req: RequestModel):
    return {"response": convert_logic_to_code(req.logic, req.language)}

@app.post("/analyze_complexity")
def analyze(req: RequestModel):
    return {"response": analyze_complexity(req.code)}

@app.post("/get_snippets")
def get_snippets_endpoint(req: RequestModel):
    return {"response": get_snippets(req.language, req.snippet)}

@app.post("/get_projects")
def get_projects_endpoint(req: RequestModel):
    return {"response": get_projects(req.level, req.topic)}

@app.post("/get_roadmaps")
def get_roadmaps_endpoint(req: RequestModel):
    return {"response": get_roadmaps(req.level, req.topic)}

@app.post("/trace_code")
def trace_code_endpoint(req: RequestModel):
    return {"response": trace_code(req.code, req.language)}
