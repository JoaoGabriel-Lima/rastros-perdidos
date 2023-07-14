def menu():
    import pygame
    import vila
    import sys
    import andamento
    import controles

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    background = pygame.image.load("./assets/GUI/menu0.jpg").convert()

    playRect = pygame.Rect(0, 0, 1200, 43)
    playRect.center = (screen.get_width()/2, 462.5)

    controlsRect = pygame.Rect(0, 0, 1200, 43)
    controlsRect.center = (screen.get_width()/2, 506)

    exitRect = pygame.Rect(0, 0, 1200, 43)
    exitRect.center = (screen.get_width()/2, 554.5)

    andamento.resetValues()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if playRect.collidepoint(mouse):
            background = pygame.image.load("./assets/GUI/menu1.jpg").convert()
            if click[0] == 1:
                controles.controles()
        elif controlsRect.collidepoint(mouse):
            background = pygame.image.load("./assets/GUI/menu2.jpg").convert()
            if click[0] == 1:
                controles.controles()
        elif exitRect.collidepoint(mouse):
            background = pygame.image.load("./assets/GUI/menu3.jpg").convert()
            if click[0] == 1:
                sys.exit()
        else:
            background = pygame.image.load("./assets/GUI/menu0.jpg").convert()
        
        pygame.display.update()
        clock.tick(60)
