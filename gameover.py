def gameover(casa, vila, texto = "Algo aconteceu e você perdeu as pistas"):
    import pygame
    import sys

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    fonte = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 25)
    textoAuxiliar = fonte.render(texto, True, (255,255,255))

    tryAgainRect = pygame.Rect(0, 0, 384, 74)
    tryAgainRect.center = (screen.get_width()/2, 390)

    gotoVilaRect = pygame.Rect(0, 0, 318, 62)
    gotoVilaRect.center = (screen.get_width()/2, 476)




    background = pygame.image.load("./assets/GUI/gameover.jpg").convert()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (0, 0))
        screen.blit(textoAuxiliar, (screen.get_width()/2 - textoAuxiliar.get_width()/2, 301))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if tryAgainRect.collidepoint(mouse):
            if click[0] == 1:
                casa()
        if gotoVilaRect.collidepoint(mouse):
            if click[0] == 1:
                vila()
        
        pygame.display.update()
        clock.tick(60)
