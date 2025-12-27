import pygame
from settings import display_settings


def set_display_mode(root_screen=None):

    target_w, target_h = display_settings.get_current_resolution()
    flags = pygame.FULLSCREEN if display_settings.is_fullscreen else 0

    if root_screen:
        root_screen = pygame.display.set_mode((target_w, target_h), flags)
    else:
        root_screen = pygame.display.set_mode((target_w, target_h), flags)

    return root_screen