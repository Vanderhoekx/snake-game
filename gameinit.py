import pygame
import random

class GameInit:
    def __init__(self):
        pygame.init()
        self.idx = 0
        self.main_height = 600
        self.main_width = 600
        self.main = pygame.display.set_mode([self.main_height, self.main_width])
        pygame.display.set_caption('Pride Snake')
        self.score_font = pygame.font.SysFont('comicsansmc', 25)
        self.clock = pygame.time.Clock()
        self.snake_size = 10
        self.snake_speed = 20
        self.food_image = pygame.image.load('assets/rainbow.png')
        self.food_image = pygame.transform.smoothscale(self.food_image, (13, 13))
        self.snake_colors = ['assets/blue.png', 'assets/green.png', 'assets/purple.png', 'assets/red.png', 'assets/yellow.png']
        self.snake_image = pygame.image.load(random.choice(self.snake_colors))
        self.snake_image = pygame.transform.smoothscale(self.snake_image, (11, 11))
        self.background = pygame.image.load('assets/land_grass04.png')
        self.background = pygame.transform.scale(self.background, (self.main_height, self.main_width))