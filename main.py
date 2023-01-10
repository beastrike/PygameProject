import pygame

pygame.init()

bg = pygame.image.load("map.png")
car = pygame.image.load("car(right).png")

window = pygame.display.set_mode((555, 555))
screen = pygame.Surface((555, 555))
start_game = True
x_car = 0
y_car = 255

while start_game == True:
    for i in  pygame.event.get():
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
    window.blit(screen, (0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(car, (x_car, y_car))
    pygame.display.update()




pygame.quit()