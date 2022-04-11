import pygame
pygame.init()
screen = pygame.display.set_mode([1240,840])
screen.fill([255, 255, 255])
my_ball = pygame.image.load('FIFA 2022 World Cup Ball.png')
x = 300
y = 300
y_speed = 10
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255,255,255], [x, y, 90, 90], 0)
    y = y + y_speed
    if y > screen.get_width():
        y = 0
    screen.blit(my_ball, [x, y])
    pygame.display.flip()
pygame.quit()
