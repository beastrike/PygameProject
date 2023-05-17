import pygame
import button
import sys


def quit_game():
    pygame.quit()
    sys.exit()


def game_over(score):
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = 30
    bg = pygame.image.load("images/GAME OVER SCREEN.png").convert_alpha()
    f1 = pygame.font.Font("FSEX300.ttf", 60)
    f2 = pygame.font.Font("FSEX300.ttf", 60)
    best_score = open("best_score.txt").read()
    text_score = f1.render(str(score), True, (254, 254, 254))
    text_best_score = f2.render(best_score, True, (254, 254, 254))
    clock = pygame.time.Clock()

    while True:
        screen.blit(bg, (0, 0))
        screen.blit(text_score, (573, 313))
        screen.blit(text_best_score, (598, 476))
        pygame.display.update()
        clock.tick(FPS)


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
