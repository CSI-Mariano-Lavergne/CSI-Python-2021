import pygame
pygame.init()

yellow = (251, 230, 78) #SCORE
red = (255, 0, 69) #food
blue = (14, 38, 250) #background color
green = (26, 245, 12) #snake
orange = (252, 180, 15) #game over


dis=pygame.display.set_mode((400, 300))
pygame.display.update()
pygame.display.set_caption("Snake Game by ML")
game_over =False
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
    pygame.draw.rect(dis, green,[200, 150, 10, 10])
    pygame.display.update()
pygame.quit()
quit()