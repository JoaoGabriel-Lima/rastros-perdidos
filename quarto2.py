import andamento
mostrarTexto = False
texto = None
textRect = None

interruptor = False
    
def quarto2(x = 8, y = 5.5):
    from functools import partial
    import pygame
    import sys
    import protagonista
    import world
    import sala2
    import camera
    import vila
    import gameover

    global andamento
    global interruptor

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Rastros Perdidos")
    clock = pygame.time.Clock()

    mapa = pygame.image.load("./assets/mapas/quarto/quarto2.png").convert_alpha()
    fimDeFase = False

    # Funções de interação
    fonte2 = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 25)
    textoAuxiliar = fonte2.render("Não pise no vidro, ache os botões e", True, (255,255,255))
    textoAuxiliar2 = fonte2.render("ligue o gerador da casa", True, (255,255,255))

    def gameOverJogo():
        if not andamento.casa2Completo:
            andamento.andamentoFase2 = [0,0,0,0,0,0]
            gameover.gameover(sala2.sala2, partial(vila.vila, 18, 3), "Parece que você esqueceu que cacos de vidro cortam...")

    def text (text, timer = 1500):
        # if inventario.checkIfItemIsSelected(1):
        global mostrarTexto
        global textRect
        global texto
        font = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 30)
        texto = font.render(text, True, (255,255,255))
        textRect = texto.get_rect()
        textRect.center = (screen.get_width()/2, screen.get_height()-50)
        mostrarTexto = True
        pygame.time.set_timer(pygame.USEREVENT, timer)

    def terminarFase():
        if andamento.casa2Completo:
            text("Nova dica desbloqueada!")
            text("É possível ver uma blusa estranha no chão", 5000)
            andamento.update(1, 1)


    def apertarBotao(index, valor):
        if not andamento.casa2Completo:
            andamento.andamentoFase2[index] = not andamento.andamentoFase2[index]
            if andamento.andamentoFase2[index]:
                text("O botão foi pressionado!")
            else:
                text("O botão foi desligado!")

    # Matrizes
    world_data = [
        [99,99,99,99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99,99,99,99],
        [99,49,99,00,00,50,55,00,9,99],
        [99,00,00,00,53,00,00,00,00,99],
        [99,51,00,00,00,00,00,00,00,99],
        [99,00,31,29,00,00,00,00,52,99],    
        [99,00,00,00,00,00,00,00,00,99],
        [99,00,00,00,00,00,00,00,00,99],
        [99,00,00,00,8,8,00,00,00,99],
        [99,99,99,99,99,99,99,99,99,99],
    ]

    no_colission_world_data = [
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,56,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,19,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,1,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
    ]

    interaction_world_data = [
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,2,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,3,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,4,00,00,00,00,1,00],
        [00,00,00,00,00,00,00,00,00,00],
    ]

    world_data_obstacles = [
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,11,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,11,00],
        [00,00,00,00,11,11,11,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,11,00,11,00,00,00],
        [00,00,11,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
    ]

    #configuração luz
    grow = 0
    min_grow = 2.4
    max_grow = 2.7
    grow_speed = 0.01
    grow_mode = 1

    # Filtro mapa sem luz
    original_light = pygame.image.load("./assets/lighting/lantern.png").convert_alpha()
    original_width, original_height = original_light.get_size()
    light = pygame.image.load("./assets/lighting/lantern.png").convert_alpha()
    light = pygame.transform.scale(original_light, (original_width*0, original_width*0))
    filterBG = pygame.surface.Surface((screen.get_width(), screen.get_height()))

    background = pygame.Surface(screen.get_size())
    background.fill((48, 44, 46))
    camera_group = camera.CameraGroup(mapa, ((screen.get_width() - mapa.get_width()) / 2), (screen.get_height() - mapa.get_height()) / 2, extra_group=andamento.buttongroupQuarto)
    quartoMundo = world.World(mapx=((screen.get_width() - mapa.get_width()) / 2), mapy=((screen.get_height() - mapa.get_height()) / 2), group=camera_group)

    inventario = protagonista.PlayerInventory(inventory=[1,2], inventorySelected=1, slots=3)
    protagonistaPlayer = protagonista.Protagonista(quartoMundo,x,y, group=camera_group, inventario=inventario)

    quartoMundo.criarObjeto(world_data)
    quartoMundo.criarObjeto(no_colission_world_data, colission=False)
    quartoMundo.criarInteracao(interaction_world_data, [0, partial(sala2.sala2, 16, 6.4), partial(apertarBotao, 3, 1), partial(apertarBotao, 4, 1), partial(apertarBotao, 5, 1)])
    quartoMundo.criarEspinho(world_data_obstacles, gameOverJogo)

    if len(andamento.listaBotoes) < 4:
        button4 = andamento.Button(1, 4, andamento.buttongroupQuarto, mapx=((screen.get_width() - mapa.get_width()) / 2), mapy=((screen.get_height() - mapa.get_height()) / 2))
        button5 = andamento.Button(1, 6, andamento.buttongroupQuarto, mapx=((screen.get_width() - mapa.get_width()) / 2), mapy=((screen.get_height() - mapa.get_height()) / 2))
        button6 = andamento.Button(3, 8, andamento.buttongroupQuarto, mapx=((screen.get_width() - mapa.get_width()) / 2), mapy=((screen.get_height() - mapa.get_height()) / 2))
        andamento.listaBotoes.append(button4)
        andamento.listaBotoes.append(button5)
        andamento.listaBotoes.append(button6)

    text("É... Não saio dessa casa viva não", 5000)

    global mostrarTexto, texto, textRect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT:
                mostrarTexto = False
                pygame.time.set_timer(pygame.USEREVENT, 0)

        screen.blit(background, (0, 0))
        camera_group.custom_draw(protagonistaPlayer)        
        protagonistaPlayer.update()

        filterBG.fill((240,255,255))
        filterBG.blit(light, ((screen.get_width() - light.get_width())/2 , (screen.get_height() - light.get_height())/2))
        if not interruptor:
            screen.blit(filterBG, (0,0), special_flags=pygame.BLEND_RGBA_SUB)


        # aumentar e diminuir a lanterna
        if inventario.checkIfItemIsSelected(2):
            if grow > max_grow:
                grow_mode = -1
            elif grow < min_grow:
                grow_mode = 1
                if grow < min_grow - 0.1:
                    grow_speed = 0.075
                else:
                    grow_speed = 0.01
            grow += grow_mode*grow_speed
            light = pygame.transform.scale(original_light, (original_width*grow, original_width*grow))
        else:
            grow_mode = -1
            grow_speed = 0.15
            if grow + grow_mode*grow_speed >= 0:
                grow += grow_mode*grow_speed
            elif grow + grow_mode*grow_speed < 0:
                grow = 0
            light = pygame.transform.scale(original_light, (original_width*grow, original_width*grow))

        #Desenhar textos e inventario
        inventario.drawSlots(screen)
        if mostrarTexto:
            screen.blit(andamento.balaofala, (screen.get_width()/2 - 500, screen.get_height()-135))
            screen.blit(texto, (screen.get_width()/2 - 460, screen.get_height()-85))

        andamento.draw(screen)

        for i in range(len(andamento.listaBotoes)):
            if andamento.andamentoFase2[i] == 1:
                andamento.listaBotoes[i].activate()
            else:
                andamento.listaBotoes[i].disable()

        if not andamento.casa2Completo and andamento.andamentoFase2.count(True) == 6:
            andamento.casa2Completo = True
            fimDeFase = True
            terminarFase()

        screen.blit(textoAuxiliar, (screen.get_width()/2 - textoAuxiliar.get_width()/2, 30))
        screen.blit(textoAuxiliar2, (screen.get_width()/2 - textoAuxiliar2.get_width()/2, 55))

        if andamento.casa2Completo:
            textoAuxiliar = fonte2.render("Casa 2 completa", True, (255,255,255))
            textoAuxiliar2 = fonte2.render("", True, (255,255,255))

        interruptor = andamento.casa2Completo

        pygame.display.update()
        clock.tick(60)