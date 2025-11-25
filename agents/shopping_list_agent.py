class ShoppingListAgent:

    def generate_shopping_list(self, recipes):
        print("   - ShoppingListAgent: Creating shopping list...")
        items = []

        for day in recipes:
            for recipe in recipes[day]:
                items.extend(recipe.get("ingredients", []))

        # Deduplicate
        return sorted(list(set(items)))
