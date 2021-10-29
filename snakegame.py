import pygame
import random
import os
os.chdir(r'C:\Users\schmi\OneDrive\Desktop\programming\python\pygame\snake game')

class SnakeGame:
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

    def player_snake(self, snake_size, snake_coord): 
        for coord in snake_coord:
            self.main.blit(self.snake_image, [coord[0], coord[1], self.snake_size, self.snake_size])
            

    def player_score(self, score):
        value = self.score_font.render('Score: ' + str(score), True, 'purple')
        self.main.blit(value, [0, 0])

    def gameloop(self):
        game_over = False
        pos_x = self.main_height // 2
        pos_y = self.main_width // 2
        pos_x_chg = 0
        pos_y_chg = 0
        high_score = 0
        snake_coords = []
        snake_length = 1
        foodx = round(random.randrange(0, self.main_width - self.snake_size) / 10) * 10
        foody = round(random.randrange(0, self.main_height - self.snake_size) / 10) * 10

        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        pos_x_chg = 0
                        pos_y_chg = -self.snake_size
                    elif event.key == pygame.K_s:
                        pos_x_chg = 0
                        pos_y_chg = self.snake_size
                    elif event.key == pygame.K_d:
                        pos_x_chg = self.snake_size
                        pos_y_chg = 0
                    elif event.key == pygame.K_a:
                        pos_x_chg = -self.snake_size
                        pos_y_chg = 0

            if pos_x >= self.main_width or pos_x < 0 or pos_y >= self.main_height or pos_y < 0:
                game_over = True

            pos_x += pos_x_chg
            pos_y += pos_y_chg
            self.main.blit(self.background, (0, 0))
            self.main.blit(self.food_image, [foodx, foody, self.snake_size, self.snake_size])
            snake = []
            snake.append(pos_x)
            snake.append(pos_y)
            snake_coords.append(snake)

            if len(snake_coords) > snake_length:
                del snake_coords[0]

            for x in snake_coords[:-1]:
                if x == snake:
                    game_over = True

            self.player_snake(self.snake_size, snake_coords)
            self.player_score(high_score)
            pygame.display.update()

            if pos_x == foodx and pos_y == foody:
                foodx = round(random.randrange(0, self.main_width - self.snake_size) / 10.0) * 10.0
                foody = round(random.randrange(0, self.main_height - self.snake_size) / 10.0) * 10.0
                snake_length += 3
                high_score += 10
                self.snake_image = pygame.image.load(random.choice(self.snake_colors))
                self.snake_image = pygame.transform.smoothscale(self.snake_image, (11, 11))
            self.clock.tick(self.snake_speed)

        with open('HighScores.txt', 'a') as scoreboard:
            print('Please enter name for scoreboard')
            player_name = input()
            scoreboard.write(player_name + ': ' + str(high_score))
            scoreboard.write('\n')

        pygame.quit()
        quit()
        
user_snake = SnakeGame()

user_snake.gameloop()
        
