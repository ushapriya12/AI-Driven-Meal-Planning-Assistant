from tools.memory_store import MemoryStore

class MemoryAgent:

    def __init__(self):
        self.db = MemoryStore()

    def get_preferences(self):
        return self.db.load_memory()

    def save_preferences_from_plan(self, plan):
        self.db.save_memory({"last_plan": plan})
