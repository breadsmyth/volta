import pygame
import settings

def handle(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.IS_RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                settings.IS_RUNNING = False