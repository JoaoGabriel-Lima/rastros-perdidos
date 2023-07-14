import pygame

pygame.init()

class Npc(pygame.sprite.Sprite):
    def __init__(self, x, y, img, group, group2, target):
        super().__init__(group)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tile = (self.image, self.rect)
        self.mask = pygame.mask.from_surface(self.image)
        self.target = target
        group2.add(self)

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y, img, group):
        super().__init__(group)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tile = (self.image, self.rect)
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class InteractionObj(pygame.sprite.Sprite):
    def __init__(self, x, y, img, group, interaction):
        super().__init__(group)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tile = (self.image, self.rect)
        self.mask = pygame.mask.from_surface(self.image)
        self.interaction = interaction

    def interact(self):
        self.interaction()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

class World():
    def __init__(self, mapx, mapy,group):
        self.mapx = mapx
        self.mapy = mapy
        self.objects_group = pygame.sprite.Group()
        self.colission_group = pygame.sprite.Group()
        self.interaction_group = pygame.sprite.Group()
        self.obstacles_group = pygame.sprite.Group()
        self.red_blocks_group = pygame.sprite.Group()
        self.group = group
        self.occupied_positions = []


    #! Adicionar collision no criarObjeto
    def criarObjeto(self, world_data, colission=True):
        for y, row in enumerate(world_data):
            for x, tile in enumerate(row):
                if tile == 99:
                    img = pygame.Surface((48,48))
                    img.fill((255,0,0))
                    img.set_alpha(0)
                    valorX = x * 48 + self.mapx
                    valorY = y * 48 + self.mapy + 48*0
                    self.occupied_positions.append((valorX, valorY))
                    obj = Objeto(valorX, valorY, img, self.group)
                    self.colission_group.add(obj)
                    self.red_blocks_group.add(obj)

                if tile != 0 and tile != 99:
                    img = pygame.image.load(f"./assets/decoracoes/{tile}.png").convert_alpha()
                    valorX = x * 48 + self.mapx
                    valorY = y * 48 + self.mapy
                    obj = Objeto(valorX, valorY, img, self.group)
                    self.occupied_positions.append((valorX, valorY))
                    self.objects_group.add(obj)
                    if colission:
                        self.colission_group.add(obj)

    def criarInteracao(self, world_data, functions):
        for y, row in enumerate(world_data):
            for x, tile in enumerate(row):
                if tile != 0:
                    img = pygame.Surface((55,55))
                    img.fill((0,0,255))
                    img.set_alpha(0)
                    valorX = x * 48 + self.mapx
                    valorY = y * 48 + self.mapy
                    # print(tile)
                    # print(functions)
                    # print(functions[tile])
                    self.occupied_positions.append((valorX, valorY))
                    obj = InteractionObj(valorX, valorY, img, self.group, functions[tile])
                    self.interaction_group.add(obj)

    def criarEspinho(self, world_data, function):
        for y, row in enumerate(world_data):
            for x, tile in enumerate(row):
                if tile != 0:
                    img = pygame.Surface((48,48))
                    img = pygame.image.load("./assets/visualEffects/vidro.png").convert_alpha()
                    valorX = x * 48 + self.mapx
                    valorY = y * 48 + self.mapy
                    obj = InteractionObj(valorX, valorY, img, self.group, function)
                    self.obstacles_group.add(obj)
        
                    
    def draw(self, screen):
        self.interaction_group.draw(screen)
        self.objects_group.draw(screen)
        self.colission_group.draw(screen)
        self.objects_group.draw(screen)





