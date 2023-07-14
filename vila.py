import andamento
mostrarTexto = False
texto = None
textRect = None
import random
import pygame

pygame.mixer.init()
musica = pygame.mixer.Sound("./assets/audio/music.mp3").play(-1).set_volume(0.1)
# pygame.mixer.Sound.set_volume(musica, 0.1)

def vila(x=13, y=5):
    import pygame
    import sys
    import protagonista
    import world
    import sala1
    import sala2
    import sala3
    import camera
    import particle
    import gameover
    from functools import partial
    import creditos

    global andamento


    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Rastros Perdidos - Jade Village")
    clock = pygame.time.Clock()

    mapa = pygame.image.load("./assets/mapas/vila/jade_village_3.png").convert()
    background = pygame.Surface(screen.get_size())
    background.fill((48, 44, 46))

    camera_group = camera.CameraGroup(mapa, 0, 0)
    vilaMundo = world.World(mapx=(0), mapy=(0), group=camera_group)


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

    # make a 32 x 19 matriz in world_data
    world_data = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00,00,00,00],
        [00,00,00,00,00,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,00,00,00,00],
        [99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99],
        [99,99,99,99,99,99,99,99,42,99,99,0,37,0,0,39,99,99,99,99,99,0,99,99,99,99,99,99,0,0,0,99],
        [99,99,99,99,99,99,99,0,0,0,44,0,0,35,34,0,99,99,99,99,99,39,99,99,99,99,99,99,0,0,0,99],
        [99,99,99,99,99,34,0,0,0,0,0,0,0,0,0,36,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99],
        [99,99,99,99,0,0,0,0,0,35,0,0,0,0,33,0,99,38,0,0,0,0,0,34,99,99,99,99,99,99,99,99],
        [99,99,99,99,0,0,0,0,0,0,0,0,0,0,0,39,99,33,99,0,0,0,0,34,99,0,0,99,99,99,99,99],
        [99,99,99,99,0,0,0,0,34,0,0,0,0,0,0,34,0,0,99,33,0,0,0,99,33,0,0,99,99,99,99,99],
        [99,0,0,0,33,0,0,0,38,0,0,0,0,0,0,41,38,0,0,0,0,0,0,0,35,0,0,0,0,0,0,99],
        [99,0,0,0,0,0,0,0,0,33,0,0,0,0,0,0,0,0,34,0,0,0,0,0,42,0,0,0,0,0,0,99],
        [99,0,0,0,0,0,0,0,0,0,34,0,0,0,0,0,0,0,0,37,0,0,0,34,0,0,0,0,99,99,99,99],
        [99,35,0,0,0,0,0,0,33,0,0,36,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99,99,99,99],
        [99,0,0,0,0,0,0,0,0,39,0,0,0,43,0,0,0,35,0,0,0,0,0,0,0,0,0,0,99,99,99,99],
        [99,99,99,99,99,0,0,0,0,37,0,0,0,0,34,0,0,0,0,0,0,0,0,0,0,0,0,0,99,0,99,99],
        [0,0,0,0,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,99,0,0,0,0,0,0,0,0,0,99],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99,99,99,99,99,99,99,99,99,99,99],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]
    world_data_collisions = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,99,0,0,0,0,99,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

    world_data_interactions = [
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    ]

    def gameOverJogo():
        if not andamento.faseFinalCompleto:
            gameover.gameover(partial(vila, 29, 7), partial(vila, 29, 7), "Talvez eu tenha que entender melhor as minhas próprias pistas...")


    vilaMundo.criarObjeto(world_data, False)
    vilaMundo.criarObjeto(world_data_collisions, True)
    vilaMundo.criarInteracao(world_data_interactions, [0, partial(sala1.sala1), partial(sala2.sala2), partial(sala3.sala3)])
    protagonista = protagonista.Protagonista(vilaMundo,x,y, group=camera_group)

    def generateRandomValues():
        randomX = random.randint(0, 31) * 48
        randomY = random.randint(3, 13) * 48
        posOcupada = False

        for b in range(len(vilaMundo.occupied_positions)):
            if vilaMundo.occupied_positions[b][0] == randomX and vilaMundo.occupied_positions[b][1] == randomY:
                posOcupada = True
                break
        if posOcupada:
            return generateRandomValues()
        else:
            return randomX, randomY

    andamento.updateIniciarFaseFinal()
    grupoNPC = pygame.sprite.Group()
    if andamento.iniciarFaseFinal:
        print("iniciar fase final")
        text("O assassino pode ser qualquer um na vila", 5000)
        for i in range(1, 11):
            randomX, randomY = generateRandomValues()
            npc_image = pygame.image.load(f"./assets/NPC/{i}.png").convert_alpha()
            flipped = random.randint(0, 1)
            if flipped == 1:
                npc_image = pygame.transform.flip(npc_image, True, False)

            target = False
            if i == 10:
                target = True

            npc = world.Npc(randomX, randomY, npc_image, group=camera_group, group2=grupoNPC, target=target)
            vilaMundo.occupied_positions.append([randomX, randomY])
            vilaMundo.occupied_positions.append([randomX + 48, randomY + 48])
            vilaMundo.occupied_positions.append([randomX, randomY + 48])
            vilaMundo.occupied_positions.append([randomX, randomY - 48])
            vilaMundo.occupied_positions.append([randomX - 48, randomY])
            vilaMundo.occupied_positions.append([randomX + 48, randomY])
            vilaMundo.occupied_positions.append([randomX - 48, randomY - 48])

    global mostrarTexto, texto, textRect
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.USEREVENT:
                mostrarTexto = False
                pygame.time.set_timer(pygame.USEREVENT, 0)

        screen.blit(background, (0, 0))
        
        camera_group.custom_draw(protagonista)
        protagonista.update()
        andamento.draw(screen)

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_SPACE]:
            for i in grupoNPC:
                if i.rect.colliderect(protagonista.rect):
                    if i.target:
                        text("FINALMENTE EU TE ENCONTREI", 5000)
                        andamento.faseFinalCompleto = True
                        creditos.credito()
                    else:
                        gameOverJogo()

        if mostrarTexto:
            screen.blit(andamento.balaofala, (screen.get_width()/2 - 500, screen.get_height()-135))
            screen.blit(texto, (screen.get_width()/2 - 460, screen.get_height()-85))

        pygame.display.update()
        clock.tick(60)
