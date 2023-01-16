import pygame
import button
import menu
pygame.init()

bg = pygame.image.load("car and map testing/map.png")
car = pygame.image.load("car and map testing/car(right).png")
menu = pygame.image.load("yandex.webp")
#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys. png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()



window = pygame.display.set_mode((555, 555))
screen = pygame.Surface((555, 555))
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
        if i.type == pygame.KEYDOWN and i.key == pygame.K_SPACE:
            menu


    screen.blit(bg, (0, 0))
    screen.blit(car, (x_car, y_car))
    screen.blit(screen, (0, 0))
    pygame.display.update()


pygame.quit()