from agents.meal_planner_agent import MealPlannerAgent
from agents.recipe_search_agent import RecipeSearchAgent
from agents.shopping_list_agent import ShoppingListAgent
from agents.memory_agent import MemoryAgent

class Orchestrator:
    def __init__(self):
        self.meal_agent = MealPlannerAgent()
        self.recipe_agent = RecipeSearchAgent()
        self.shopping_agent = ShoppingListAgent()
        self.memory_agent = MemoryAgent()

    def run(self, user_request):
        print("\n[1] Retrieving user preferences...")
        preferences = self.memory_agent.get_preferences()

        print("[2] Creating weekly meal plan...")
        meal_plan = self.meal_agent.generate_meal_plan(user_request, preferences)

        print("[3] Fetching recipes for each meal...")
        recipes = self.recipe_agent.search_recipes(meal_plan)

        print("[4] Generating optimized shopping list...")
        shopping_list = self.shopping_agent.generate_shopping_list(recipes)

        print("[5] Saving updated preferences...")
        self.memory_agent.save_preferences_from_plan(meal_plan)

        return {
            "meal_plan": meal_plan,
            "recipes": recipes,
            "shopping_list": shopping_list
        }
