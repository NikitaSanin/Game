class BaseEffect:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def modify_ap(self, current_ap):
        """Змінює кількість АП на початку ходу."""
        return current_ap

    def on_turn_end(self):
        """Зменшує тривалість ефекту."""
        self.duration -= 1
        return self.duration > 0  # Повертає True, якщо ефект ще діє