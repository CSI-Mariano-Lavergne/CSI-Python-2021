import time
import pygame
pygame.init()

yellow = (251, 230, 78) #SCORE
red = (255, 0, 69) #food
blue = (14, 38, 250) #background color
green = (26, 245, 12) #snake
orange = (252, 180, 15) #game over

dis_width = 400
dis_height = 300
dis=pygame.display.set_mode((400, 300))

pygame.display.set_caption("Snake Game by ML")
game_over =False


clock = pygame.time.Clock()
snake_speed = 15
snake_block = 10

font_style = pygame.font.SysFont(None, 50)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

def gameloop():
    game_over = False
    game_close = False

    x1 = dis_width/2    
    y1 = dis_height/2

    x1_change = 0
    y1_change = 0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("YOU LOST! Press Q-Quit or P-Play Again", orange)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_p:
                        gameloop()


    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.type == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.type == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.type == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True            
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    pygame.draw.rect(dis, green,[x1, y1, snake_block, snake_block])

    pygame.display.update()

    clock.tick(snake_speed)

pygame.quit()
quit()