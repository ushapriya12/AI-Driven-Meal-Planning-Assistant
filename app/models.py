from pydantic import BaseModel

class MealPlanRequest(BaseModel):
    user_id: str
    instruction: str
    realtime_data: dict | None = None
