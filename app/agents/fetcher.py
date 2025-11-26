import asyncio

# Replace with real web search / recipe API usage
async def web_search_recipes(query: str) -> list:
    await asyncio.sleep(0.05)
    if not query:
        return []
    return [
        {"title": f"{query} - Simple Recipe", "url": "https://example.com/recipe1", "ingredients": ["ingredient A", "ingredient B"]}
    ]

class FetcherAgent:
    def __init__(self):
        pass

    async def find_recipes(self, query: str) -> list:
        return await web_search_recipes(query)
