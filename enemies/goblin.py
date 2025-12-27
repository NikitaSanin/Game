from enemies.base_enemy import BaseEnemy

class Goblin(BaseEnemy):
    def __init__(self, x, y):
        super().__init__(
            x, y,
            hp=40,
            max_ap=3,
            name="Goblin Scout",
            damage=5,
            color=(100, 255, 100),
            scale=0.5
        )