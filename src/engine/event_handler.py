import pygame
import settings

keys = ['up', 'left', 'down', 'right', 'use', 'fire', 'menu', 'inv', 'status', 'next', 'prev']

def handle(events):
    for event in events:
        if event.type == pygame.QUIT:
            settings.IS_RUNNING = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                settings.IS_RUNNING = False

            # Parse keys
            for key in keys:
                if event.key == pygame.key.key_code(settings.OPTIONS[key].lower()):
                    key_to_event(key)()

        if event.type == pygame.KEYUP:
            # Parse stop pressing keys
            for key in keys:
                if event.key == pygame.key.key_code(settings.OPTIONS[key].lower()):
                    key_to_event(key)(stopped=True)


def key_to_event(key):
    match key:
        case 'up': return k_up
        case 'left': return k_left
        case 'right': return k_right
        case 'down': return k_down
        case 'use': return k_use
        case 'fire': return k_fire
        case 'menu': return k_menu
        case 'inv': return k_inv
        case 'status': return k_status
        case 'next': return k_next
        case 'prev': return k_prev

        case _: print(f"event_handler: unknown option '{key}'")

# Key events
def k_up(stopped=False):
    if stopped:
        pass
    pass

def k_left(stopped=False):
    if stopped:
        pass
    pass

def k_down(stopped=False):
    if stopped:
        pass
    pass

def k_right(stopped=False):
    if stopped:
        pass
    pass

def k_use(stopped=False):
    if stopped:
        pass
    pass

def k_fire(stopped=False):
    if stopped:
        pass
    pass

def k_menu(stopped=False):
    if stopped:
        pass
    pass

def k_inv(stopped=False):
    if stopped:
        pass
    pass

def k_status(stopped=False):
    if stopped:
        pass
    pass

def k_next(stopped=False):
    if stopped:
        pass
    pass

def k_prev(stopped=False):
    if stopped:
        pass
    pass
