import pygame


def main_menu(b_ratio):
    screen  = pygame.display.get_surface()

    #Loading Images
    background_original = pygame.image.load("images/background.png")
    title_original = pygame.image.load("images/dominion_logo.png")
    build_button = [pygame.image.load("images/build_button.png"), pygame.image.load("images/build_button_pressed.png")]
    saved_button = [pygame.image.load("images/saved_button.png"), pygame.image.load("images/saved_button_pressed.png")]
    close_button = [pygame.image.load("images/close_button.png"), pygame.image.load("images/close_button_pressed.png")]

    build_button = [pygame.transform.scale(build_button[0], (build_button[0].get_size()[0] * b_ratio, build_button[0].get_size()[1] * b_ratio)), pygame.transform.scale(build_button[1], (build_button[0].get_size()[0] * b_ratio, build_button[0].get_size()[1] * b_ratio))]
    saved_button = [pygame.transform.scale(saved_button[0], (saved_button[0].get_size()[0] * b_ratio, saved_button[0].get_size()[1] * b_ratio)), pygame.transform.scale(saved_button[1], (saved_button[0].get_size()[0] * b_ratio, saved_button[0].get_size()[1] * b_ratio))]
    close_button = [pygame.transform.scale(close_button[0], (close_button[0].get_size()[0] * b_ratio, close_button[0].get_size()[1] * b_ratio)), pygame.transform.scale(close_button[1], (close_button[0].get_size()[0] * b_ratio, close_button[0].get_size()[1] * b_ratio))]

    running = True
    print("This is the main menu")

    # Learning how to use fonts in the game
    test_font = pygame.font.Font("fonts/dominion.ttf", 30)
    text1 = test_font.render("INTRIGUE", True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = screen.get_rect().center

    ratio = (pygame.display.Info().current_w / background_original.get_size()[0], pygame.display.Info().current_h / background_original.get_size()[1])
    background = pygame.transform.scale(background_original, (background_original.get_size()[0] * ratio[0], background_original.get_size()[1] * ratio[1]))
    scale = pygame.display.Info().current_w * .75 / title_original.get_size()[0]
    if scale > .5:
        scale = .5
    title = pygame.transform.scale(title_original, (title_original.get_size()[0] * scale, title_original.get_size()[1] * scale))

    title_Rect = title.get_rect()
    build_Rect = build_button[0].get_rect()
    saved_Rect = saved_button[0].get_rect()
    close_Rect = close_button[0].get_rect()

    build_button_pic = build_button[0]
    saved_button_pic = saved_button[0]
    close_button_pic = close_button[0]


    while running:
        for event in pygame.event.get(pygame.VIDEORESIZE):
            ratio = (pygame.display.Info().current_w / background_original.get_size()[0], pygame.display.Info().current_h / background_original.get_size()[1])
            background = pygame.transform.scale(background_original, (background_original.get_size()[0] * ratio[0], background_original.get_size()[1] * ratio[1]))
            scale = pygame.display.Info().current_w * .75 / title_original.get_size()[0]
            if scale > .5:
                scale = .5
            title = pygame.transform.scale(title_original, (title_original.get_size()[0] * scale, title_original.get_size()[1] * scale))
            title_Rect = title.get_rect()
            print(scale)

        screen.blit(background, (0,0))

        title_Rect.center = (screen.get_rect().center[0], title.get_size()[1] * .6)
        build_Rect.center = (screen.get_rect().center[0], title_Rect.y + title_Rect.h + build_Rect.h/2)
        saved_Rect.center = (screen.get_rect().center[0], build_Rect.center[1] + saved_Rect.h + 20)
        close_Rect.center = (screen.get_rect().center[0], saved_Rect.center[1] + close_Rect.h + 20)

        screen.blit(title, title_Rect)
        screen.blit(build_button_pic, build_Rect)
        screen.blit(saved_button_pic, saved_Rect)
        screen.blit(close_button_pic, close_Rect)

        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if build_Rect.x < pygame.mouse.get_pos()[0] < build_Rect.x + build_Rect.w and build_Rect.y < pygame.mouse.get_pos()[1] < build_Rect.y + build_Rect.h:
                    build_button_pic = build_button[1]
                if saved_Rect.x < pygame.mouse.get_pos()[0] < saved_Rect.x + saved_Rect.w and saved_Rect.y < pygame.mouse.get_pos()[1] < saved_Rect.y + saved_Rect.h:
                    saved_button_pic = saved_button[1]
                if close_Rect.x < pygame.mouse.get_pos()[0] < close_Rect.x + close_Rect.w and close_Rect.y < pygame.mouse.get_pos()[1] < close_Rect.y + close_Rect.h:
                    close_button_pic = close_button[1]

        for event in pygame.event.get(pygame.MOUSEBUTTONUP):
            if event.type == pygame.MOUSEBUTTONUP:
                build_button_pic = build_button[0]
                saved_button_pic = saved_button[0]
                close_button_pic = close_button[0]
                if build_Rect.x < pygame.mouse.get_pos()[0] < build_Rect.x + build_Rect.w and build_Rect.y < pygame.mouse.get_pos()[1] < build_Rect.y + build_Rect.h:
                    return 1
                if saved_Rect.x < pygame.mouse.get_pos()[0] < saved_Rect.x + saved_Rect.w and saved_Rect.y < pygame.mouse.get_pos()[1] < saved_Rect.y + saved_Rect.h:
                    pass
                if close_Rect.x < pygame.mouse.get_pos()[0] < close_Rect.x + close_Rect.w and close_Rect.y < pygame.mouse.get_pos()[1] < close_Rect.y + close_Rect.h:
                    return -1

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                return -1

        pygame.display.flip()