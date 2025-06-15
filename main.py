from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.service.agent_runner import process_prompt
from app.service.flow_runner import run_flow_with_prompt

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/run/agent")
async def run_with_agent(input: PromptInput):
    prompt = input.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is empty")
    result = await process_prompt(prompt)
    return {
        "mode": "agent",
        "status": "ok",
        "result": result
    }

@app.post("/run/flow")
async def run_with_flow(input: PromptInput):
    prompt = input.prompt.strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is empty")
    result = await run_flow_with_prompt(prompt)
    return {
        "mode": "flow",
        "status": "ok",
        "result": result
    }
