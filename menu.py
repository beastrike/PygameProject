import pygame
import button


def Menu_screeen():
    # create game window
    SCREEN_WIDTH = 555
    SCREEN_HEIGHT = 555

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_paused = False
    menu_state = "main"

    font = pygame.font.SysFont("arialblack", 40)

    # define colours
    TEXT_COL = (255, 255, 255)

    # load button images
    resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
    options_img = pygame.image.load("images/button_options.png").convert_alpha()
    quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
    audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
    back_img = pygame.image.load('images/button_back.png').convert_alpha()

    # create button instances
    resume_button = button.Button(200, 125, resume_img, 1)
    options_button = button.Button(186, 250, options_img, 1)
    quit_button = button.Button(233, 375, quit_img, 1)
    audio_button = button.Button(100, 200, audio_img, 1)
    back_button = button.Button(220, 300, back_img, 1)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    # game loop
    run = True
    while run:

        screen.fill((52, 78, 91))

        # check if game is paused
        if game_paused == True:
            # check menu state
            if menu_state == "main":
                # draw pause screen buttons
                if resume_button.draw(screen):
                    game_paused = False
                if options_button.draw(screen):
                    menu_state = "options"
                if quit_button.draw(screen):
                    run = False
            # check if the options menu is open
            if menu_state == "options":
                # draw the different options buttons
                if audio_button.draw(screen):
                    print("Audio Settings")
                if back_button.draw(screen):
                    menu_state = "main"
        else:
            draw_text("", font, TEXT_COL, 160, 250)

        # event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_paused = True
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    Menu_screeen()
    pygame.quit()
