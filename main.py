import pygame
import sys
import display_manager
from menus import main_menu, settings_menu, level_select_menu
from game_loop import play_level
from shop_menu import shop_menu


def main():
    pygame.init()
    root_screen = display_manager.set_display_mode()
    pygame.display.set_caption("Demeo")

    current_state = "MENU"

    while True:
        if current_state == "MENU":
            res = main_menu(root_screen)
            if res == "QUIT":
                break

            elif res == "Start":
                out = play_level(root_screen, "level_1.txt")
                if out == "QUIT": break

            elif res == "Levels":
                current_state = "LEVELS"
            elif res == "Settings":
                current_state = "SETTINGS"
            elif res == "Shop":
                current_state = "SHOP"

        elif current_state == "SHOP":
            res = shop_menu(root_screen)
            if res == "QUIT":
                break
            elif res == "MENU":
                current_state = "MENU"

        elif current_state == "LEVELS":
            res = level_select_menu(root_screen)
            if res == "QUIT":
                break
            elif res == "MENU":
                current_state = "MENU"
            else:
                out = play_level(root_screen, res)
                current_state = "MENU"
                if out == "QUIT": break
        elif current_state == "SETTINGS":
            ns = settings_menu(root_screen)
            if ns == "QUIT": break
            root_screen = ns
            current_state = "MENU"

    pygame.quit()
    sys.exit()
if __name__ == "__main__":
    main()