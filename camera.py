from settings import TILE_SIZE

class Camera:
    def __init__(self):
        self.zoom = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.speed = 15

    def world_to_screen(self, gx, gy):
        screen_x = (gx * TILE_SIZE * self.zoom) + self.offset_x
        screen_y = (gy * TILE_SIZE * self.zoom) + self.offset_y
        return screen_x, screen_y

    def screen_to_world(self, mx, my):
        gx = int((mx - self.offset_x) / (TILE_SIZE * self.zoom))
        gy = int((my - self.offset_y) / (TILE_SIZE * self.zoom))
        return gx, gy