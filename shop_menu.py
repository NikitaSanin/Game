import pygame
from settings import *
from player_data import player_data, SHOP_COLORS


def shop_menu(root_screen):
    font = pygame.font.SysFont('Arial', 24)
    title_font = pygame.font.SysFont('Arial', 40, bold=True)

    btn_back = pygame.Rect(20, 20, 100, 40)

    while True:
        root_screen.fill(COLOR_BG)
        sw, sh = root_screen.get_size()
        cx = sw // 2

        title = title_font.render("МАГАЗИН СКІНІВ", True, (255, 255, 255))
        root_screen.blit(title, (cx - title.get_width() // 2, 20))

        coins_txt = font.render(f"Ваші монети: {player_data.coins}", True, (255, 215, 0))
        root_screen.blit(coins_txt, (sw - coins_txt.get_width() - 20, 20))

        pygame.draw.rect(root_screen, (200, 50, 50), btn_back)
        b_txt = font.render("Назад", True, (255, 255, 255))
        root_screen.blit(b_txt, (btn_back.centerx - b_txt.get_width() // 2, btn_back.centery - b_txt.get_height() // 2))

        start_y = 100
        item_height = 60

        buttons = []

        for i, item in enumerate(SHOP_COLORS):
            y = start_y + i * (item_height + 10)
            rect = pygame.Rect(cx - 250, y, 500, item_height)

            pygame.draw.rect(root_screen, (50, 50, 60), rect)
            pygame.draw.rect(root_screen, (100, 100, 100), rect, 2)

            color_preview = pygame.Rect(rect.x + 10, rect.y + 10, 40, 40)
            pygame.draw.rect(root_screen, item["color"], color_preview)

            name_t = font.render(item["name"], True, (255, 255, 255))
            root_screen.blit(name_t, (rect.x + 60, rect.centery - name_t.get_height() // 2))

            btn_action = pygame.Rect(rect.right - 140, rect.y + 10, 130, 40)
            buttons.append((btn_action, item))

            if item["id"] == player_data.current_color_id:
                pygame.draw.rect(root_screen, (100, 100, 100), btn_action)
                t = font.render("Одягнуто", True, (200, 200, 200))

            elif item["id"] in player_data.unlocked_colors:
                pygame.draw.rect(root_screen, (50, 200, 50), btn_action)
                t = font.render("Обрати", True, (0, 0, 0))

            else:
                can_afford = player_data.coins >= item["price"]
                col = (255, 215, 0) if can_afford else (150, 50, 50)
                pygame.draw.rect(root_screen, col, btn_action)
                t = font.render(f"Купити ({item['price']})", True, (0, 0, 0))

            root_screen.blit(t, (btn_action.centerx - t.get_width() // 2, btn_action.centery - t.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: return "QUIT"

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mp = pygame.mouse.get_pos()

                if btn_back.collidepoint(mp): return "MENU"

                for btn, item in buttons:
                    if btn.collidepoint(mp):
                        if item["id"] == player_data.current_color_id:
                            pass

                        elif item["id"] in player_data.unlocked_colors:
                            player_data.current_color_id = item["id"]

                        else:
                            if player_data.coins >= item["price"]:
                                player_data.coins -= item["price"]
                                player_data.unlocked_colors.append(item["id"])
                                player_data.current_color_id = item["id"]
                            else:
                                print("Недостатньо грошей!")

        pygame.display.flip()