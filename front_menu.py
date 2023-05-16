import pygame
import button
import sys


def quit_game():
    pygame.quit()
    sys.exit()


def front_menu():
    # create game window
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    FPS = 30
    menu_state = "main"
    font = pygame.font.SysFont("arialblack", 40)
    TEXT_COL = (255, 255, 255)
    start_img = pygame.image.load("images/start_btn.png").convert_alpha()
    exit_img = pygame.image.load("images/exit_btn.png").convert_alpha()
    back_gr = pygame.image.load("images/start menu.png").convert_alpha()

    start_button = button.Button(250, 550, start_img, 1)
    exit_button = button.Button(650, 550, exit_img, 1)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        screen.blit(img, (x, y))

    clock = pygame.time.Clock()
    while True:
        screen.blit(back_gr, (0, 0))
        if menu_state == "main":
            if start_button.draw(screen):
                return
            if exit_button.draw(screen):
                quit_game()

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
    front_menu()
    quit_game()
