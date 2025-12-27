from effects.base_effect import BaseEffect

class SlowEffect(BaseEffect):
    def __init__(self, duration):
        super().__init__("Slow", duration)

    def modify_ap(self, current_ap):
        return max(0, current_ap - 1)