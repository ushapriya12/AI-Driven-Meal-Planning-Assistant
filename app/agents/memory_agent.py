import json
from pathlib import Path
import asyncio

class MemoryAgent:
    def __init__(self, store_path: str = './memory_store.json'):
        self.path = Path(store_path)
        if not self.path.exists():
            self.path.write_text(json.dumps({}), encoding='utf-8')

    async def _read_store(self) -> dict:
        return await asyncio.to_thread(lambda: json.loads(self.path.read_text(encoding='utf-8')))

    async def _write_store(self, data: dict):
        await asyncio.to_thread(lambda: self.path.write_text(json.dumps(data, indent=2), encoding='utf-8'))

    async def read_preferences(self, user_id: str) -> dict | None:
        data = await self._read_store()
        return data.get(user_id)

    async def update_from_plan(self, user_id: str, plan: dict):
        data = await self._read_store()
        # store only a small summary to keep things simple
        data[user_id] = {"last_plan_summary": plan}
        await self._write_store(data)
