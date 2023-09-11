import engine.options as opts
import engine.event_handler as events
import pygame
import settings

pygame.init()
settings.OPTIONS = opts.read()

screen = pygame.display.set_mode(settings.OPTIONS['resolution'])
fps_clock = pygame.time.Clock()

while settings.IS_RUNNING:
    events.handle(pygame.event.get())

pygame.quit()