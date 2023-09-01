import engine.options as opts
import pygame

pygame.init()
opt_dict = opts.read()

print(opt_dict)

pygame.quit()