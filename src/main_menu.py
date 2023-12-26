import pygame


def main_menu():
    screen  = pygame.display.get_surface()
    background = pygame.image.load("images/background.png")

    # Getting the logo to the right size
    title = pygame.image.load("images/dominion_logo.png")
    title = pygame.transform.scale(title, (title.get_size()[0] * .40, title.get_size()[1] * .40))
    titleRect = title.get_rect()
    titleRect.center = (screen.get_rect().center[0], 120)


    running = True
    print("This is the main menu")

    # Learning how to use fonts in the game
    test_font = pygame.font.Font("fonts/dominion.ttf", 30)
    text1 = test_font.render("INTRIGUE", True, (0,0,0))
    textRect1 = text1.get_rect()
    textRect1.center = screen.get_rect().center

    while running:
        screen.blit(background, (0,0))
        screen.blit(title, titleRect)

        screen.blit(text1, textRect1)


        for event in pygame.event.get(pygame.MOUSEBUTTONDOWN):
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("The mouse clicked")

        for event in pygame.event.get(pygame.QUIT):
            if event.type == pygame.QUIT:
                exit()

        pygame.display.flip()