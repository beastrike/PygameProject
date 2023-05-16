import pygame
import button
import sys


def quit_game():
    pygame.quit()
    sys.exit()


def Menu_screeen():
    # create game window
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    FPS = 30
    menu_state = "main"
    font = pygame.font.SysFont("arialblack", 40)
    TEXT_COL = (255, 255, 255)
    resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    options_img = pygame.image.load("images/button_options.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()
    delivery_back_image = pygame.image.load('images/delivery_back.jpg').convert_alpha()

    resume_button = button.Button(100, 80, resume_img, 1)
    options_button = button.Button(100, 250, options_img, 1)
    quit_button = button.Button(133, 420, quit_img, 1)
    audio_button = button.Button(100, 120, audio_img, 1)
    back_button = button.Button(100, 295, back_img, 1)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    clock = pygame.time.Clock()
    while True:
        screen.fill((255, 255, 0))
        if menu_state == "main":
            if resume_button.draw(screen):
                return
            if options_button.draw(screen):
                menu_state = "options"
            if quit_button.draw(screen):
                quit_game()
        screen.blit(delivery_back_image, (500, 275))
        if menu_state == "options":
            if audio_button.draw(screen):
                print("Audio Settings")
            if back_button.draw(screen):
                menu_state = "main"

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = True
            if event.type == pygame.QUIT:
                quit_game()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    pygame.init()
    Menu_screeen()
    quit_game()
