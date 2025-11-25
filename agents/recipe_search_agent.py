from tools.recipe_search_tool import recipe_search

class RecipeSearchAgent:

    def search_recipes(self, meal_plan):
        print("   - RecipeSearchAgent: Searching recipes...")
        results = {}
        for day, meals in meal_plan.items():
            results[day] = []
            for meal in meals:
                recipe = recipe_search(meal)
                results[day].append(recipe)
        return results
