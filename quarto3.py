import andamento
mostrarTexto = False
texto = None
textRect = None

interruptor = False
    
def quarto3(x = 8, y = 5.5):
    from functools import partial
    import pygame
    import sys
    import protagonista
    import world
    import sala3
    import camera
    import vila
    import fantasmas
    import gameover

    global andamento
    global interruptor

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Rastros Perdidos")
    clock = pygame.time.Clock()

    mapa = pygame.image.load("./assets/mapas/quarto/quarto3.png").convert_alpha()
    fimDeFase = False

    # Funções de interação
    fonte2 = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 25)
    textoAuxiliar = fonte2.render("Desvie dos fanstamas e", True, (255,255,255))
    textoAuxiliar2 = fonte2.render("Ache a pista perdida", True, (255,255,255))

    def gameOverJogo():
        if not andamento.casa3Completo:
            gameover.gameover(sala3.sala3, partial(vila.vila, 29, 7), "Fantasmas não são tão legais assim...")

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
        if not andamento.casa3Completo:
            text("É possível ver uma lente de contato azul", 3000)
            andamento.update(2, 1)
            andamento.casa3Completo = True

    # Matrizes
    world_data = [
        [99,99,99,99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99,99,99,99],
        [99,61,99,99,65,00,00,00,99,99],
        [99,00,00,00,00,00,53,11,00,99],
        [99,00,00,00,00,00,00,00,63,99],
        [99,6,00,00,00,00,29,66,00,99],    
        [99,00,00,00,00,00,00,00,00,99],
        [99,45,00,00,00,00,00,00,00,99],
        [99,00,00,45,00,45,00,00,00,99],
        [99,99,99,99,99,99,99,99,99,99],
    ]

    no_colission_world_data = [
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,1,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,19,00,00,00,00,00],
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
        [00,00,00,00,00,00,00,2,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [000,00,00,00,00,00,00,00,1,00],
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
    camera_group = camera.CameraGroup(mapa, ((screen.get_width() - mapa.get_width()) / 2), (screen.get_height() - mapa.get_height()) / 2)
    quartoMundo = world.World(mapx=((screen.get_width() - mapa.get_width()) / 2), mapy=((screen.get_height() - mapa.get_height()) / 2), group=camera_group)

    inventario = protagonista.PlayerInventory(inventory=[1,2], inventorySelected=1, slots=3)
    protagonistaPlayer = protagonista.Protagonista(quartoMundo,x,y, group=camera_group, inventario=inventario)

    quartoMundo.criarObjeto(world_data)
    quartoMundo.criarObjeto(no_colission_world_data, colission=False)
    quartoMundo.criarInteracao(interaction_world_data, [0, partial(sala3.sala3, 16, 6.4), terminarFase])

    text("Pelo menos esses não correm atrás de mim... né?", 3000)
    
    fantasma1 = fantasmas.Fantasma(quartoMundo, 5, 5, camera_group, protagonistaPlayer, 1, "FixedX", 4, 7, 6)
    fantasma2 = fantasmas.Fantasma(quartoMundo, 5, 5, camera_group, protagonistaPlayer, 1.1, "FixedY", 2, 6.5, 5)
    fantasma3 = fantasmas.Fantasma(quartoMundo, 5, 5, camera_group, protagonistaPlayer, 1.5, "FixedX", 3, 7, 4)

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

        filterBG.fill((100,70,100))
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

        screen.blit(textoAuxiliar, (screen.get_width()/2 - textoAuxiliar.get_width()/2, 30))
        screen.blit(textoAuxiliar2, (screen.get_width()/2 - textoAuxiliar2.get_width()/2, 55))

        if andamento.casa3Completo:
            textoAuxiliar = fonte2.render("Casa 3 completa", True, (255,255,255))
            textoAuxiliar2 = fonte2.render("", True, (255,255,255))

        fantasma1.update()
        fantasma2.update()
        fantasma3.update()

        if pygame.sprite.collide_mask(protagonistaPlayer, fantasma1) or pygame.sprite.collide_mask(protagonistaPlayer, fantasma2) or pygame.sprite.collide_mask(protagonistaPlayer, fantasma3):
            gameOverJogo()

        interruptor = andamento.casa3Completo
        pygame.display.update()
        clock.tick(60)