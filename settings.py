TILE_SIZE = 40
GRID_SIZE_X = 20
GRID_SIZE_Y = 20
UI_HEIGHT = 100

COLOR_BG = (20, 20, 30)
COLOR_GRID = (50, 50, 60)
COLOR_PLAYER = (50, 150, 255)
COLOR_TEXT = (255, 255, 255)
COLOR_VISITED = (30, 30, 50)
COLOR_WALL = (100, 100, 100)

COLOR_UI_BG = (255, 255, 255)
COLOR_UI_BORDER = (0, 0, 0)
COLOR_UI_TEXT_RED = (200, 0, 0)

class DisplaySettings:
    def __init__(self):
        self.resolutions = [
            (800, 600),
            (1024, 768),
            (1280, 720),
            (1920, 1080)
        ]
        self.current_res_index = 0
        self.is_fullscreen = False

    def get_current_resolution(self):
        return self.resolutions[self.current_res_index]

    def next_resolution(self):
        self.current_res_index = (self.current_res_index + 1) % len(self.resolutions)

    def toggle_fullscreen(self):
        self.is_fullscreen = not self.is_fullscreen

display_settings = DisplaySettings()