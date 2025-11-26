from app.tools.shopping_tool import ShoppingTool

class ShoppingAgent:
    def __init__(self):
        self.tool = ShoppingTool()

    async def generate_shopping_list(self, plan: dict) -> dict:
        items = []
        for m in plan.get('meals', []):
            for r in m.get('recipes', []):
                items.extend(r.get('ingredients', []))

        # Consolidate quantities (simple count)
        consolidated = {}
        for it in items:
            consolidated[it] = consolidated.get(it, 0) + 1

        availability = await self.tool.check_availability(list(consolidated.keys()))
        return {"items": consolidated, "availability": availability}
