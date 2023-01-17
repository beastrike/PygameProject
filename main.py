import pygame
import button
import menu
pygame.init()

bg = pygame.image.load("car and map testing/map.png")
car = pygame.image.load("car and map testing/car(right).png")




window = pygame.display.set_mode((1280, 720))
screen = pygame.Surface((1280, 720))
start_game = True
x_car = 0
y_car = 255

while start_game == True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            start_game = False
        if i.type == pygame.KEYDOWN and i.key == pygame.K_s:
            y_car += 25
        if i.type == pygame.KEYDOWN and i.key == pygame.K_d:
            x_car += 25
        if i.type == pygame.KEYDOWN and i.key == pygame.K_a:
            x_car -= 25
        if i.type == pygame.KEYDOWN and i.key == pygame.K_w:
            y_car -= 25
        if i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
            menu.Menu_screeen()


    screen.blit(bg, (0, 0))
    screen.blit(car, (x_car, y_car))
    screen.blit(screen, (0, 0))
    pygame.display.update()


pygame.quit()