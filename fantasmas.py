import pygame

pygame.init()

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, world, x, y, group, player, speed = 1, mode = "Follow", n1 = 0, n2 = 0, nFixed = 0):
        super().__init__(group)
        self.world = world

        self.initAnimation()
        self.rect = self.image.get_rect()
        self.rect.x = x * 48 + self.world.mapx
        self.rect.y = y * 48 + self.world.mapy + 48
        self.mask = pygame.mask.from_surface(self.image)
        self.target = player
        self.speed = speed
        self.base_speed = speed
        self.mode = mode
        self.n1 = n1
        self.n2 = n2
        self.nFixed = nFixed

        self.GoUp = False
        self.GoRight = False

        if self.mode == "FixedX":
            self.rect.x = self.nFixed * 48 + self.world.mapx
            self.rect.y = self.n1 * 48 + self.world.mapy + 48
        elif self.mode == "FixedY":
            self.rect.y = self.nFixed * 48 + self.world.mapy + 48
            self.rect.x = self.n1 * 48 + self.world.mapx 
            

    def initAnimation(self):
        self.sprites = []
        self.animations = {'walking': [], 'vanish': []}
        self.animation_speed = 0.2
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/1.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/2.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/3.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/4.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/5.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/6.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/7.png"))
        self.sprites.append(pygame.image.load("./assets/personagens/fantasma/8.png"))

        for i in range(0, 8):
            self.animations['walking'].append(self.sprites[i])

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def animate(self, animation):
        animation = self.animations[animation]

        self.current_sprite += self.animation_speed
        if self.current_sprite >= len(animation):
            self.current_sprite = 0
        
        self.image = animation[int(self.current_sprite)]

    def followPlayer(self):
        if self.rect.x > self.target.rect.x:
            self.rect.x -= self.speed
        elif self.rect.x < self.target.rect.x:
            self.rect.x += self.speed
        if self.rect.y > self.target.rect.y:
            self.rect.y -= self.speed
        elif self.rect.y < self.target.rect.y:
            self.rect.y += self.speed

        # self.speed vary accordig to the distance between the ghost and the player
        # calculate distance 

        dist = pygame.math.Vector2(self.rect.x, self.rect.y).distance_to((self.target.rect.x, self.target.rect.y))
        self.speed = self.base_speed + dist / 100

        # for obj in self.world.red_blocks_group:
            # if pygame.sprite.collide_mask(self, obj):
            #     # self.image.fill((0,0,255))
            #     break
            # else:
            #     # self.image.fill((255,0,0))
    def FixedX(self):
        
        if self.rect.y >= self.n2 * 48 + self.world.mapy + 48:
            self.GoUp = True
        elif self.rect.y <= self.n1 * 48 + self.world.mapy + 48:
            self.GoUp = False


        if self.GoUp:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        


    def FixedY(self):
        if self.rect.x >= self.n2 * 48 + self.world.mapx:
            self.GoRight = True
        elif self.rect.x <= self.n1 * 48 + self.world.mapx:
            self.GoRight = False

        if self.GoRight:
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        
    def update(self):
        if self.mode == "Follow":
            self.followPlayer()
        elif self.mode == "FixedX":
            self.FixedX()
        elif self.mode == "FixedY":
            self.FixedY()
        self.animate('walking')
           
