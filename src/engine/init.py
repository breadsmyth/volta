import engine.options as opts
import engine.event_handler as events
import pygame
import settings

pygame.init()

settings.OPTIONS = opts.read()
settings.RESOLUTION = (
    settings.OPTIONS['resolution'][0] * settings.OPTIONS['zoom'],
    settings.OPTIONS['resolution'][1] * settings.OPTIONS['zoom'])

screen = pygame.display.set_mode(settings.RESOLUTION)
fps_clock = pygame.time.Clock()

while settings.IS_RUNNING:
    events.handle(pygame.event.get())

pygame.quit()