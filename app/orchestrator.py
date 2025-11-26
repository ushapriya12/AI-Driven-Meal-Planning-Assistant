import asyncio
from app.agents.planner import PlannerAgent
from app.agents.fetcher import FetcherAgent
from app.agents.shopping import ShoppingAgent
from app.agents.memory_agent import MemoryAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent()
        self.fetcher = FetcherAgent()
        self.shopping = ShoppingAgent()
        self.memory = MemoryAgent()

    async def handle_user_message(self, user_id: str, message: str, realtime_data: dict | None = None):
        # 0. Read stored preferences (if any)
        user_prefs = await self.memory.read_preferences(user_id)

        # 1. Create plan skeleton using PlannerAgent
        plan = await self.planner.create_plan(user_id, message, user_prefs, realtime_data)

        # 2. Fetch recipes in parallel (for each meal)
        recipe_tasks = []
        for i, day_meal in enumerate(plan.get('meals', [])):
            query = day_meal.get('query', '')
            recipe_tasks.append(self.fetcher.find_recipes(query))

        recipes = await asyncio.gather(*recipe_tasks) if recipe_tasks else []

        # Attach recipe results back to plan (safe indexing)
        for i, r in enumerate(recipes):
            if i < len(plan.get('meals', [])):
                plan['meals'][i]['recipes'] = r

        # 3. Consolidate shopping list
        shopping_list = await self.shopping.generate_shopping_list(plan)

        # 4. Update memory from plan
        await self.memory.update_from_plan(user_id, plan)

        # 5. Return aggregated response
        return {"plan": plan, "shopping_list": shopping_list}
