class ShoppingTool:
    def __init__(self):
        # Mock catalog; replace with real API in production
        self.store_catalog = {
            "ingredient a": {"price": 50, "available": True},
            "ingredient b": {"price": 30, "available": True},
            "oatmeal with fruits": {"price": 120, "available": True},
            "grilled chicken salad": {"price": 250, "available": True},
            "pasta with vegetables": {"price": 80, "available": True},
        }

    async def check_availability(self, items: list) -> dict:
        res = {}
        for it in items:
            key = it.lower()
            info = self.store_catalog.get(key)
            if info:
                res[it] = {"available": info['available'], "price": info['price']}
            else:
                res[it] = {"available": False, "price": None}
        return res
