import pygame
from settings import Settings
import game_functions as gf

def run_game():
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode(settings.screen_width, settings.screen_height)
    pygame.display.set_caption("PacMan Battle Royale YEET")


    running = True
    while running:
        #Here we will add the game functions
        pygame.display.update()
