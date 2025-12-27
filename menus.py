import pygame
from settings import *
from player_data import player_data
from utils import get_available_levels
import display_manager


def main_menu(root_screen):
    font = pygame.font.SysFont('Arial', 40)
    title_font = pygame.font.SysFont('Arial', 80, bold=True)
    ui_font = pygame.font.SysFont('Arial', 20)

    while True:
        root_screen.fill(COLOR_BG)
        sw, sh = root_screen.get_size();
        cx = sw // 2

        t = title_font.render("DEMEO CLONE", True, COLOR_PLAYER)
        root_screen.blit(t, (cx - t.get_width() // 2, 80))

        coins_txt = ui_font.render(f"Монети: {player_data.coins}", True, (255, 215, 0))
        root_screen.blit(coins_txt, (sw - coins_txt.get_width() - 20, 20))

        btns = [
            (pygame.Rect(cx - 120, 200, 240, 50), "Грати", "Start"),
            (pygame.Rect(cx - 120, 260, 240, 50), "Магазин", "Shop"),
            (pygame.Rect(cx - 120, 320, 240, 50), "Рівні", "Levels"),
            (pygame.Rect(cx - 120, 380, 240, 50), "Налаштування", "Settings"),
            (pygame.Rect(cx - 120, 440, 240, 50), "Вихід", "QUIT")
        ]

        for b, txt, act in btns:
            col = (100, 80, 20) if act == "Shop" else (70, 70, 90)
            pygame.draw.rect(root_screen, col, b)
            ts = font.render(txt, True, (255, 255, 255))
            root_screen.blit(ts, (b.centerx - ts.get_width() // 2, b.centery - ts.get_height() // 2))

        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "QUIT"
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mp = pygame.mouse.get_pos()
                for b, txt, act in btns:
                    if b.collidepoint(mp): return act
        pygame.display.flip()


def settings_menu(root_screen):
    font = pygame.font.SysFont('Arial', 30)
    while True:
        root_screen.fill(COLOR_BG)
        sw, sh = root_screen.get_size();
        cx = sw // 2

        rw, rh = display_settings.get_current_resolution()
        is_fs = display_settings.is_fullscreen

        btn_res = pygame.Rect(cx - 150, 200, 300, 50)
        btn_fs = pygame.Rect(cx - 150, 270, 300, 50)
        btn_back = pygame.Rect(cx - 150, 340, 300, 50)

        # Кнопка Розширення
        pygame.draw.rect(root_screen, (70, 70, 90), btn_res)
        root_screen.blit(font.render(f"Розширення: {rw}x{rh}", True, (255, 255, 255)), (btn_res.x + 20, btn_res.y + 10))

        # Кнопка Повний екран
        pygame.draw.rect(root_screen, (70, 70, 90), btn_fs)
        root_screen.blit(font.render(f"Повний екран: {'ТАК' if is_fs else 'НІ'}", True, (255, 255, 255)),
                         (btn_fs.x + 20, btn_fs.y + 10))

        # Кнопка Назад
        pygame.draw.rect(root_screen, (70, 70, 90), btn_back)
        root_screen.blit(font.render("Назад", True, (255, 255, 255)), (btn_back.centerx - 30, btn_back.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "QUIT"
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mp = pygame.mouse.get_pos()

                if btn_res.collidepoint(mp):
                    display_settings.next_resolution()
                    root_screen = display_manager.set_display_mode(root_screen)

                if btn_fs.collidepoint(mp):
                    display_settings.toggle_fullscreen()
                    root_screen = display_manager.set_display_mode(root_screen)

                if btn_back.collidepoint(mp): return root_screen
        pygame.display.flip()


def level_select_menu(root_screen):
    font = pygame.font.SysFont('Arial', 20)
    files = get_available_levels()
    btn_back = pygame.Rect(10, 10, 80, 40)
    while True:
        root_screen.fill(COLOR_BG)
        sw, sh = root_screen.get_size()
        pygame.draw.rect(root_screen, (200, 50, 50), btn_back)
        root_screen.blit(font.render("Back", True, (255, 255, 255)), (20, 20))
        level_btns = []
        for i, f in enumerate(files):
            btn = pygame.Rect(sw // 2 - 100, 80 + i * 50, 200, 40)
            level_btns.append((btn, f))
            pygame.draw.rect(root_screen, (70, 70, 90), btn)
            t = font.render(f, True, (255, 255, 255))
            root_screen.blit(t, (btn.centerx - t.get_width() // 2, btn.centery - t.get_height() // 2))
        for e in pygame.event.get():
            if e.type == pygame.QUIT: return "QUIT"
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mp = pygame.mouse.get_pos()
                if btn_back.collidepoint(mp): return "MENU"
                for btn, f in level_btns:
                    if btn.collidepoint(mp): return f
        pygame.display.flip()