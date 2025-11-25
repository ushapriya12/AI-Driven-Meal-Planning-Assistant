from agents.orchestrator import Orchestrator

if __name__ == "__main__":
    orchestrator = Orchestrator()
    
    user_request = "Plan a healthy vegetarian weekly meal schedule."
    
    result = orchestrator.run(user_request)

    print("\n===== FINAL OUTPUT =====")
    print("Meal Plan:", result["meal_plan"])
    print("Recipes:", result["recipes"])
    print("Shopping List:", result["shopping_list"])
