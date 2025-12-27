import os
import pickle
from settings import GRID_SIZE_X, GRID_SIZE_Y

game_log = []


def add_log(*messages):
    full_message = " ".join(map(str, messages))
    game_log.append(full_message)
    print(f"[LOG]: {full_message}")


def load_level_matrix(filename="levels/level_1.txt"):
    if not os.path.exists(filename):
        print(f"[ERROR] Файл {filename} не знайдено! Використовую запасну карту.")
        return [
            [1 if x == 0 or x == GRID_SIZE_X - 1 or y == 0 or y == GRID_SIZE_Y - 1 else 0 for x in range(GRID_SIZE_X)]
            for y in range(GRID_SIZE_Y)]

    matrix = []
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                cleaned_line = line.strip()
                row = []
                for char in cleaned_line:
                    if char.isdigit():
                        row.append(int(char))
                if row:
                    matrix.append(row)
    except Exception as e:
        print(f"[ERROR] Помилка читання: {e}")

    if len(matrix) < 2:
        return [
            [1 if x == 0 or x == GRID_SIZE_X - 1 or y == 0 or y == GRID_SIZE_Y - 1 else 0 for x in range(GRID_SIZE_X)]
            for y in range(GRID_SIZE_Y)]

    return matrix

def get_available_levels():
    if not os.path.exists("levels"):
        return []

    files = [f for f in os.listdir("levels") if f.endswith(".txt")]
    files.sort()
    return files