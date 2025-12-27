import pygame
from settings import UI_HEIGHT


class InputManager:
    def __init__(self, camera):
        self.camera = camera
        self.is_dragging = False
        self.last_mouse = (0, 0)

    def process_camera_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:  self.camera.offset_x += self.camera.speed
        if keys[pygame.K_RIGHT]: self.camera.offset_x -= self.camera.speed
        if keys[pygame.K_UP]:    self.camera.offset_y += self.camera.speed
        if keys[pygame.K_DOWN]:  self.camera.offset_y -= self.camera.speed

    def handle_event(self, event, root_screen_size):
        sw, sh = root_screen_size

        # ZOOM
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                self.camera.zoom *= 1.1
            elif event.y < 0:
                self.camera.zoom /= 1.1
            self.camera.zoom = max(0.5, min(self.camera.zoom, 3.0))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
            self.is_dragging = True;
            self.last_mouse = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 2:
            self.is_dragging = False
        elif event.type == pygame.MOUSEMOTION and self.is_dragging:
            mx, my = pygame.mouse.get_pos()
            self.camera.offset_x += mx - self.last_mouse[0]
            self.camera.offset_y += my - self.last_mouse[1]
            self.last_mouse = (mx, my)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: return "MENU"
            if event.key == pygame.K_SPACE: return "SPACE"
            if event.key == pygame.K_w: return "MOVE_UP"
            if event.key == pygame.K_s: return "MOVE_DOWN"
            if event.key == pygame.K_a: return "MOVE_LEFT"
            if event.key == pygame.K_d: return "MOVE_RIGHT"

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mx, my = pygame.mouse.get_pos()
            ui_y = sh - UI_HEIGHT

            if my > ui_y:
                skill_w = sw - 140
                if mx > skill_w: return "BTN_END_TURN"

                col_w = skill_w // 6
                if my > ui_y + 25:
                    col_index = int(mx // col_w)
                    if col_index == 0: return "BTN_FIREBALL"
                    if col_index == 1: return "BTN_HEAL"
                    if col_index == 2: return "BTN_ICESHARD"
                    if col_index == 3: return "BTN_LIGHTNING"
            else:
                gx, gy = self.camera.screen_to_world(mx, my)
                return ("CLICK_WORLD", gx, gy)

        return None