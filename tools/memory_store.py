import json
import os

class MemoryStore:

    def __init__(self, file_path="memory.json"):
        self.file_path = file_path

    def load_memory(self):
        if not os.path.exists(self.file_path):
            return {}
        with open(self.file_path, "r") as f:
            return json.load(f)

    def save_memory(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)
