def controles():
    import pygame
    import vila
    import sys
    import andamento

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    background = pygame.image.load("./assets/GUI/controles.jpg").convert()

    playRect = pygame.Rect(0, 0, 345, 58)
    playRect.center = (screen.get_width()/2, 586)

    andamento.resetValues()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if playRect.collidepoint(mouse):
            if click[0] == 1:
                vila.vila()
        
        pygame.display.update()
        clock.tick(60)
