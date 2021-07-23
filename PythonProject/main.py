import pygame
import random
import sys
from settings import Settings

pygame.init()
ai_settings= Settings()
screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height),)

pygame.display.set_caption('Snake Eater')

clock = ai_settings.clock
snake1 = ai_settings.snakelength

font_style = pygame.font.SysFont(" ", 40)
score_font = pygame.font.SysFont(" ", 40)

def snake(snake1, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, (255, 255, 255), [x[0], x[1], snake1, snake1])

def show_score(score):
    value = pygame.font.SysFont("", 40).render("Your Score: " + str(score), True, (255, 0, 0))
    screen.blit(value,value.get_rect(midtop = screen.get_rect().midtop))

def message(msg, color):
    msg1 = font_style.render(msg, True, color)
    screen.blit(msg1,msg1.get_rect(midbottom = screen.get_rect().center))

def rungame():

    x1 = ai_settings.screen_width / 2
    y1 = ai_settings.screen_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    snake_height = 1

    food_x = round(random.randrange(0, ai_settings.screen_width - snake1) / 10.0) * 10.0
    food_y = round(random.randrange(0, ai_settings.screen_height - snake1) / 10.0) * 10.0

    game_over = False
    game_close = False
    while not game_over:

        while game_close == True:
            screen.fill(ai_settings.bg_color)
            message("You lost!", (213, 50, 80))

            show_score(snake_height - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT :
                    sys.exit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = 10
                    x1_change = 0

        if x1 >= ai_settings.screen_width or x1 < 0 or y1 >= ai_settings.screen_height or y1 < 0:

            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(ai_settings.bg_color)
        pygame.draw.rect(screen, (255, 255, 255), [food_x, food_y, snake1, snake1])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > snake_height:
            del snake_List[0]

        for x in range(snake_height):
            if x == snake_Head:
                game_close = True

        snake(snake1, snake_List)
        show_score(snake_height - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, ai_settings.screen_width - snake1) / 10.0) * 10.0
            food_y = round(random.randrange(0, ai_settings.screen_height - snake1) / 10.0) * 10.0
            snake_height += 1

        clock.tick(ai_settings.snakespeed)

    pygame.quit()
    quit()


rungame()