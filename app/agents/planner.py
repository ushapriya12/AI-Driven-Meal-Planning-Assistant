import asyncio
import json

# Replace this stub with your LLM integration (OpenAI, etc.)
async def llm_call(prompt: str) -> str:
    await asyncio.sleep(0.05)
    payload = {
        "meals": [
            {"meal": "Breakfast", "query": "oatmeal with fruits"},
            {"meal": "Lunch", "query": "grilled chicken salad"},
            {"meal": "Dinner", "query": "pasta with vegetables"}
        ]
    }
    return json.dumps(payload)

class PlannerAgent:
    def __init__(self):
        pass

    async def create_plan(self, user_id: str, message: str, user_prefs: dict | None = None, realtime_data: dict | None = None) -> dict:
        # Build a prompt (for a real LLM)
        prompt = f"Create a meal plan. Message: {message}. Prefs: {user_prefs}. Realtime: {realtime_data}"
        raw = await llm_call(prompt)
        return json.loads(raw)
