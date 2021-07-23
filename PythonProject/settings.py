import pygame.time


class Settings():

    def __init__(self):

        # Screen settings
        self.screen_width = 1500
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.snakespeed=10
        self.snakelength = 10
    clock= pygame.time.Clock()
    # fonts= pygame.font.SysFont("",40)