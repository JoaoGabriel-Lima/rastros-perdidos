Interruptor = True
mostrarTexto = False
texto = None
textRect = None
import andamento
def quarto1(x = 2.25, y = 5.5):
    global andamento
    import pygame
    import sys
    import protagonista
    import world
    import sala1
    import camera
    import vila
    import gameover
    from functools import partial

    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Rastros Perdidos")
    clock = pygame.time.Clock()

    mapa = pygame.image.load("./assets/mapas/quarto/quarto1.png").convert_alpha()

    fonte = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 35)
    fonte2 = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 25)
    textoAuxiliar = fonte2.render("Ache todos os papéis antes que se percam", True, (255,255,255))
    fimDeFase = False

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

    # Configuração do mapa e da classe World
    background = pygame.Surface(screen.get_size())
    background.fill((48, 44, 46))
    camera_group = camera.CameraGroup(mapa, ((screen.get_width() - mapa.get_width()) / 2), ((screen.get_height() - mapa.get_height()) / 2))

    quarto = world.World(mapx=((screen.get_width() - mapa.get_width()) / 2), mapy=((screen.get_height() - mapa.get_height()) / 2), group=camera_group)

    world_data = [
        [99,99,99,99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99,99,99,99],
        [99,26,99,28,99,99,99,27,99,99],
        [99,00,00,00,00,00,00,00,00,99],
        [99,00,00,00,00,00,00,00,00,99],
        [99,00,00,00,00,00,00,000,2,99],    
        [99,00,00,00,00,00,29,31,00,99],
        [99,00,00,00,00,00,00,00,00,99],
        [99,00,00,00,00,00,00,00,00,99],
        [99,99,99,99,99,99,99,99,99,99],
    ]

    no_colission_world_data = [
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,19,00,00,00,00,00],
        [00,21,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
    ]

    interaction_world_data = [
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,2,00,00,00,00,4,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,3,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,5,00,00],
        [00,1,00,00,00,00,00,00,00,00],
        [00,00,00,00,00,00,00,00,00,00],
    ]

    def text (text):
        if inventario.checkIfItemIsSelected(1):
            global mostrarTexto
            global textRect
            global texto
            font = pygame.font.Font('./assets/GUI/VCRosdNEUE.ttf', 30)
            texto = font.render(text, True, (255,255,255))
            textRect = texto.get_rect()
            textRect.center = (screen.get_width()/2, screen.get_height()-50)
            mostrarTexto = True
            pygame.time.set_timer(pygame.USEREVENT, 1500)

    def interactPaper(paperNumber, texto = "Papel encontrado!"):
        if inventario.checkIfItemIsSelected(1): 
            if paperNumber in andamento.andamentoFase:
                text("Parece que já peguei esse papel...")
            else:
                andamento.andamentoFase.append(paperNumber)
                text(texto)

    # Instanciando objetos e o player
    quarto.criarObjeto(world_data)
    quarto.criarObjeto(no_colission_world_data, False)
    quarto.criarInteracao(interaction_world_data, [0, partial(sala1.sala1, 4, 7.4), partial(interactPaper, 4), partial(interactPaper, 5), partial(interactPaper, 6),  partial(interactPaper, 7)])
    inventario = protagonista.PlayerInventory(inventory=[1,2], inventorySelected=0, slots=3)
    protagonistaPlayer = protagonista.Protagonista(quarto,x,y, group=camera_group, inventario=inventario)


    global mostrarTexto, texto, textRect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT:
                mostrarTexto = False
                pygame.time.set_timer(pygame.USEREVENT, 0)


        screen.blit(background, (0, 0))

        # Desenhar o mapa e atualizar a posição do player
        camera_group.custom_draw(protagonistaPlayer)
        protagonistaPlayer.update()

        # Desenhar a iluminação do mapa
        filterBG.fill((200,220,220))
        filterBG.blit(light, ((screen.get_width() - light.get_width())/2 , (screen.get_height() - light.get_height())/2))
        if not Interruptor:
            screen.blit(filterBG, (0,0), special_flags=pygame.BLEND_RGBA_SUB)


        # Aumentar e diminuir a lanterna
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

        # Desenhar inventário
        inventario.drawSlots(screen)

        #Desenhar interações
        if mostrarTexto:
            screen.blit(andamento.balaofala, (screen.get_width()/2 - 500, screen.get_height()-135))
            screen.blit(texto, (screen.get_width()/2 - 460, screen.get_height()-85))

        # Desenhar andamento do jogo
        andamento.draw(screen)
        andamento.casa1Update()
        textoTimer = fonte2.render(f"{int(andamento.timerCasa1/60)}:{int(andamento.timerCasa1%60):02d}", True, (255,255,255))
        screen.blit(textoAuxiliar, (screen.get_width()/2 - textoAuxiliar.get_width()/2, 30))
        screen.blit(textoTimer, (screen.get_width()/2 - textoTimer.get_width()/2,95))
        
        textoAndamentoFase = fonte.render(f"{len(andamento.andamentoFase)}/{andamento.valorTotalAndamento}", True, (255,255,255))
        screen.blit(textoAndamentoFase, (screen.get_width()/2 - textoAndamentoFase.get_width()/2,60))
        if not fimDeFase and len(andamento.andamentoFase) == andamento.valorTotalAndamento:
            fimDeFase = True
            andamento.casa1Completo = True
            textoAuxiliar = fonte2.render("Um som de cadeado pode ser escutado", True, (255,255,255))
        
        if int(andamento.timerCasa1) == 0:
            andamento.andamentoFase = []
            andamento.timerCasa1 = andamento.timerCasa1Total
            andamento.casa1Completo = False
            fimDeFase = False
            gameover.gameover(sala1.sala1, partial(vila.vila, 2, 6.4), "Os papéis se perderam! Você perdeu a pista")

        pygame.display.update()
        clock.tick(60)
