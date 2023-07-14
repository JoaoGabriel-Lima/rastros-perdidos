def credito():
    import pygame

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 700))
    clock = pygame.time.Clock()

    fonte = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 25)
    fonte2 = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 20)




    background = pygame.image.load("./assets/GUI/credito.png").convert()
    grade = pygame.image.load("./assets/GUI/grade.png").convert_alpha()

    titulo1 = fonte.render("CRIADORES", True, (255,255,255))
    texto1 = fonte2.render("JOÃO GABRIEL LIMA MARINHO", True, (255,255,255))
    texto2 = fonte2.render("LARISSA YUMI NAKASHIMA", True, (255,255,255))

    # titulo2 = fonte.render("COLABORADORES", True, (255,255,255))


    titulo3 = fonte.render("AGRADECIMENTO ESPECIAL", True, (255,255,255))
    texto3 = fonte2.render("RAFAEL AMPARO", True, (255,255,255))
    texto5 = fonte2.render("JADE MENDES", True, (255,255,255))
    texto6 = fonte2.render("RICCO", True, (255,255,255))
    texto7 = fonte2.render("NATHALIA", True, (255,255,255))

    texto4 = fonte.render("OBRIGADO POR JOGAR", True, (255,255,255))

    creditos = [[titulo1, texto1, texto2], [titulo3, texto3, texto5, texto6, texto7], [texto4]]

    y = -701
    ycredito = 700

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(background, (-1, 0))
        screen.blit(grade, (2, y))

        # go to menu if press ESC
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            import menu
            menu.menu()
        
        if y < 0:
            y += 1.3

        for i in range(len(creditos)):
            for j in range(len(creditos[i])):
                y_grupos = creditos[i][j].get_height() + 10
                y_entre_grupos = 125
                y_entre_textos = 30
                if j == 0:
                    screen.blit(creditos[i][j], ((screen.get_width() - 214) - creditos[i][j].get_width()/2, ycredito + y_entre_textos*j + y_entre_grupos*i + y_grupos*i - 10))
                else:
                    screen.blit(creditos[i][j], ((screen.get_width() - 214) - creditos[i][j].get_width()/2, ycredito + y_entre_textos*j + y_entre_grupos*i + y_grupos*i))

        # screen.blit(textoAuxiliar, (screen.get_width()/2 - textoAuxiliar.get_width()/2, 301))

        if ycredito > 200:
            ycredito -= 1

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        pygame.display.update()
        clock.tick(60)
