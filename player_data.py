SHOP_COLORS = [
    {"id": "default", "name": "Classic Blue", "color": (50, 150, 255), "price": 0},
    {"id": "red",     "name": "Fire Red",     "color": (255, 50, 50),  "price": 2},
    {"id": "purple",  "name": "Void Purple",  "color": (150, 0, 200),  "price": 5},
    {"id": "gold",    "name": "Golden Legend","color": (255, 215, 0),  "price": 10},
    {"id": "shadow",  "name": "Shadow Black", "color": (30, 30, 30),   "price": 20},
]

class PlayerData:
    def __init__(self):
        self.coins = 0
        self.unlocked_colors = ["default"] # Список ID куплених кольорів
        self.current_color_id = "default"  # ID поточного кольору

    def get_current_color_rgb(self):
        for item in SHOP_COLORS:
            if item["id"] == self.current_color_id:
                return item["color"]
        return (50, 150, 255)

player_data = PlayerData()