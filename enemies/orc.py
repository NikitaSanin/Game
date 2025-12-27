from enemies.base_enemy import BaseEnemy

class Orc(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(
            x, y,
            hp=60,
            max_ap=2,
            name="Orc Warrior",
            damage=15,
            color=(0, 100, 50),
            scale=0.9
        )