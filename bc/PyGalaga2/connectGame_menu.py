import pygame
from connect_menu_btnfunc import *

pygame.init()
pygame.init()
pygame.key.set_repeat(500, 50)

display_width = 600
display_height = 1000

gameDisplay = pygame.display.set_mode((display_width, display_height))


def button_connect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 195 + 215 > mouse[0] > 195 and 500 + 50 > mouse[1] > 500:
        s = pygame.Surface((210, 50))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (195, 500))
        if click[0] == 1:
            action_connectTo_multi()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((215, 50))
        s.set_alpha(0)
        gameDisplay.blit(s, (195, 500))


def button_back_connect():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if 20 + 81 > mouse[0] > 20 and 15 + 67 > mouse[1] > 15:
        s = pygame.Surface((81, 67))
        s.set_alpha(50)
        s.fill((200, 0, 0))
        gameDisplay.blit(s, (20, 15))
        if click[0] == 1:
            action_back_to_multi_from_connect()
            pygame.quit()
            quit()
    else:
        s = pygame.Surface((81, 67))
        s.set_alpha(0)
        gameDisplay.blit(s, (20, 15))


def inputbox():
    screen = pygame.display.set_mode((600, 1000))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(53, 428, 490, 35)
    active = False
    text = ''
    done = False
    img = pygame.image.load('menu_connect_to_game.png')

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, (255, 255, 0))
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(img, (0, 0))
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        button_connect()
        button_back_connect()
        # Blit the input_box rect.
        pygame.draw.rect(screen, (255, 255, 0), input_box, 2)

        pygame.display.flip()
        clock.tick(30)


def connect_menu():
    pygame.display.set_caption('Terran Defenders')

    white = (255, 255, 255)

    clock = pygame.time.Clock()
    crashed = False
    img = pygame.image.load('menu_connect_to_game.png')

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

        gameDisplay.fill((white))
        gameDisplay.blit(img, (0, 0))
        pygame.display.flip()

        inputbox()

        clock.tick(60)

    pygame.quit()
    quit()


if __name__ == '__main__':
    #pygame.init()
    connect_menu()
    pygame.quit()

