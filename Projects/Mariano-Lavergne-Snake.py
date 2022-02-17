import pygame
pygame.init()

yellow = (251, 230, 78) #SCORE
red = (255, 0, 69) #food
blue = (14, 38, 250) #background color
green = (26, 245, 12) #snake
orange = (252, 180, 15) #game over


dis=pygame.display.set_mode((400, 300))
pygame.display.set_caption("Snake Game by ML")
game_over =False

x1 = 200
y1 = 150

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.type == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.type == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.type == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
                
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)

    pygame.draw.rect(dis, green,[x1, y1, 10, 10])

    pygame.display.update()

    clock.tick(30)
pygame.quit()
quit()