import pygame

def selection_menu(b_ratio):
    print("This is the selection menu")

    screen = pygame.display.get_surface()

    # Loading Images
    background_original = pygame.image.load("images/background.png")
    back_button = [pygame.image.load("images/back_button.png"), pygame.image.load("images/back_button_pressed.png")]
    back_button = [pygame.transform.scale(back_button[0], (back_button[0].get_size()[0] * b_ratio, back_button[0].get_size()[1] * b_ratio)), pygame.transform.scale(back_button[1], (back_button[0].get_size()[0] * b_ratio, back_button[0].get_size()[1] * b_ratio))]

    ratio = (pygame.display.Info().current_w / background_original.get_size()[0], pygame.display.Info().current_h / background_original.get_size()[1])
    background = pygame.transform.scale(background_original, (background_original.get_size()[0] * ratio[0], background_original.get_size()[1] * ratio[1]))

    back_Rect = back_button[0].get_rect()

    back_button_pic = back_button[0]

    running = True

    while(running):
        for event in pygame.event.get(pygame.VIDEORESIZE):
            ratio = (pygame.display.Info().current_w / background_original.get_size()[0], pygame.display.Info().current_h / background_original.get_size()[1])
            background = pygame.transform.scale(background_original, (background_original.get_size()[0] * ratio[0], background_original.get_size()[1] * ratio[1]))

        screen.blit(background, (0, 0))

        back_Rect.center = (back_Rect.w * .75, back_Rect.h * .75)

        screen.blit(back_button_pic, back_Rect)

        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_Rect.x < pygame.mouse.get_pos()[0] < back_Rect.x + back_Rect.w and back_Rect.y < pygame.mouse.get_pos()[1] < back_Rect.y + back_Rect.h:
                    back_button_pic = back_button[1]

        for event in pygame.event.get(pygame.MOUSEBUTTONUP):
            if event.type == pygame.MOUSEBUTTONUP:
                back_button_pic = back_button[0]
                if back_Rect.x < pygame.mouse.get_pos()[0] < back_Rect.x + back_Rect.w and back_Rect.y < pygame.mouse.get_pos()[1] < back_Rect.y + back_Rect.h:
                    return 0

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                return -1

        pygame.display.flip()