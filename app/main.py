import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.orchestrator import Orchestrator

app = FastAPI(title="AI Meal Planner Chatbot")
orch = Orchestrator()

class ChatRequest(BaseModel):
    user_id: str
    message: str
    realtime_data: dict | None = None

@app.post('/chat')
async def chat(req: ChatRequest):
    try:
        response = await orch.handle_user_message(req.user_id, req.message, req.realtime_data)
        return {"ok": True, "response": response}
    except Exception as e:
        # Return error for debugging in dev. Remove stack traces in production.
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/health')
async def health():
    return {"status": "ok"}
