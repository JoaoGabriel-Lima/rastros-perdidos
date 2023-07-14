import pygame

pygame.init()

class PlayerInventory():
    def __init__(self, inventory = [1,0,2], inventorySelected = 0, slots = 3):
        self.inventory = inventory
        self.inventorySelected = inventorySelected
        self.slots = slots

    def checkIfItemIsSelected(self, item):
        if len(self.inventory) > self.inventorySelected:
            if self.inventory[self.inventorySelected] == item:
                return True
            else:
                return False
        else:
            return False
    def select_inventory(self, number):
        self.inventorySelected = number
    
    def drawSlots(self, screen):
        slotImage = pygame.image.load("assets/inventory/inventory2.png").convert()
        slotImageSelected = pygame.image.load("assets/inventory/inventorySelected.png").convert()
        for i in range(0, self.slots):
            slotRect = slotImage.get_rect()
            slotRect.x = screen.get_width()-slotImage.get_width()-10
            slotRect.y = (slotImage.get_width()+5)*i+10
            if i == self.inventorySelected:
                screen.blit(slotImageSelected, slotRect)
            else:
                screen.blit(slotImage, slotRect)
            if len(self.inventory) > i and self.inventory[i] != 0:
                item = self.inventory[i]
                itemImage = pygame.image.load("assets/inventory/items/"+str(item)+".png").convert_alpha()
                itemRect = itemImage.get_rect()
                itemRect.x = slotRect.x + (slotImage.get_width()-itemImage.get_width())/2
                itemRect.y = slotRect.y + (slotImage.get_height()-itemImage.get_height())/2
                screen.blit(itemImage, itemRect)

class Protagonista(pygame.sprite.Sprite):
    def __init__(self, world, x, y, group, inventario = None):
        super().__init__(group)

        # player animation function
        self.initAnimation()
        self.initDustAnimation()

        # player movement variables
        self.direction = pygame.math.Vector2()
        self.inventario = inventario
        self.space_released = False
        self.world = world
        self.speed = 5 
        
        # player position variables
        self.mask = pygame.mask.from_surface(pygame.image.load("./assets/personagens/mask.png").convert_alpha())
        self.rect = self.image.get_rect(midbottom = (x * 48 + self.world.mapx, y * 48 + self.world.mapy + 48*2))
        self.position = pygame.math.Vector2(x * 48 + self.world.mapx, y * 48 + self.world.mapy + 48*2)

    def select_inventory(self):
        if self.inventario != None:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.inventario.select_inventory(0)
            if keys[pygame.K_2]:
                self.inventario.select_inventory(1)
            if keys[pygame.K_3]:
                self.inventario.select_inventory(2)
            if keys[pygame.K_4]:
                self.inventario.select_inventory(3)
            if keys[pygame.K_5]:
                self.inventario.select_inventory(4)
            if keys[pygame.K_6]:
                self.inventario.select_inventory(5)
            if keys[pygame.K_7]:
                self.inventario.select_inventory(6)
            if keys[pygame.K_8]:
                self.inventario.select_inventory(7)
            if keys[pygame.K_9]:
                self.inventario.select_inventory(8)
            if keys[pygame.K_0]:
                self.inventario.select_inventory(9)

    def initAnimation(self):
        self.sprites = []
        self.animations = {'idle': [], 'walking': [], 'walkingUp': [], 'walkingDown': []}
        self.animation_speed = 0.5
        self.status = 'idle'
        self.facing_right = True

        sprite_sheet = pygame.image.load("./assets/personagens/protagonista3.png").convert_alpha()
        for i in range(0, 24):
            self.sprites.append(sprite_sheet.subsurface((i * 48, 0, 48, 62)))
        
        for i in range(0, 8):
            self.animations['walking'].append(self.sprites[i])

        for i in range(16, 20):
            self.animations['walkingDown'].append(self.sprites[i])

        for i in range(20, 24):
            self.animations['walkingUp'].append(self.sprites[i])
        
        self.animations['idle'].append(self.sprites[0])

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

    def animate(self, animation):
        animation = self.animations[animation]

        self.current_sprite += self.animation_speed
        if self.current_sprite >= len(animation):
            self.current_sprite = 0
        
        image = animation[int(self.current_sprite)]
        if self.facing_right:
            self.image = image
        else:
            self.image = pygame.transform.flip(image, True, False)
        
    def get_status(self):
        if self.direction.x == 1:
            self.status = 'walking'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == -1:
            self.status = 'walking'
            self.facing_right = False
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.y == 1:
            self.status = 'walkingDown'
            self.animations['idle'][0] = (self.sprites[16])
        elif self.direction.y == -1:
            self.status = 'walkingUp'
            self.animations['idle'][0] = (self.sprites[20])
        elif self.direction.x == 1/1.4142 and self.direction.y == 1/1.4142:
            self.status = 'walking'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == -1/1.4142 and self.direction.y == 1/1.4142:
            self.status = 'walking'
            self.facing_right = False
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == 1/1.4142 and self.direction.y == -1/1.4142:
            self.status = 'walking'
            self.facing_right = True
            self.animations['idle'][0] = (self.sprites[0])
        elif self.direction.x == -1/1.4142 and self.direction.y == -1/1.4142:
            self.status = 'walking'
            self.facing_right = False
            self.animations['idle'][0] = (self.sprites[0])
        else:
            self.status = 'idle'
    
    def player_input(self):
        keys = pygame.key.get_pressed()

        dx = keys[pygame.K_d] - keys[pygame.K_a]
        dy = keys[pygame.K_s] - keys[pygame.K_w]
        self.direction = pygame.math.Vector2(dx, dy)
        if dx != 0 and dy != 0:
            self.direction /= 1.4142


        self.position += self.direction * self.speed
        self.rect.x = round(self.position.x)
        self.rect.y = round(self.position.y) 
         
        for obj in self.world.colission_group:
            if pygame.sprite.collide_mask(self, obj):
                self.current_sprite = 0
                self.position -= self.direction * (self.speed+0)
                self.rect.x = round(self.position.x)
                self.rect.y = round(self.position.y) 
                break

        for sprite in self.world.interaction_group:
            keys = pygame.key.get_pressed()
            if pygame.sprite.collide_mask(self, sprite) and keys[pygame.K_SPACE] and self.space_released:
                self.space_released = False
                sprite.interact()
                break
            elif not keys[pygame.K_SPACE]:
                self.space_released = True

        for sprite in self.world.obstacles_group:
            if pygame.sprite.collide_mask(self, sprite):
                sprite.interact()
                break

    def initDustAnimation(self):
        self.dust_sprites = []
        self.dust_animations = {'idle': []}
        self.dust_animation_speed = 0.1
        self.dust_status = 'idle'

        self.dust_sprites.append(pygame.image.load("./assets/visualEffects/dust2/1.png").convert_alpha())
        self.dust_sprites.append(pygame.image.load("./assets/visualEffects/dust2/2.png").convert_alpha())
        self.dust_sprites.append(pygame.image.load("./assets/visualEffects/dust2/3.png").convert_alpha())
        self.dust_sprites.append(pygame.image.load("./assets/visualEffects/dust2/4.png").convert_alpha())

        for i in range(0, 4):
            self.dust_animations['idle'].append(self.dust_sprites[i])
        
        self.dust_current_sprite = 0
        self.dust_image = self.dust_sprites[self.dust_current_sprite]

    def dust_animate(self):
        animationDust = self.dust_animations['idle']

        self.dust_current_sprite += self.dust_animation_speed
        if self.dust_current_sprite >= len(animationDust):
            self.dust_current_sprite = 0
        
        self.dust_image = animationDust[int(self.dust_current_sprite)]
        self.dust_imageScaled = pygame.transform.scale(self.dust_image, (self.dust_image.get_width()*3, self.dust_image.get_height()*3))
        
        # pos = self.screen.get_width()/2 - self.dust_image.get_width()/2 - 30, self.screen.get_height()/2 - self.dust_image.get_height()/2 + 25
        # self.screen.blit(self.dust_imageScaled, pos)
        # if self.facing_right:
        # else:
        #     pos = self.screen.get_width()/2 - self.dust_image.get_width()/2, self.screen.get_height()/2 - self.dust_image.get_height()/2
        #     self.screen.blit(pygame.transform.flip(self.dust_imageScaled, True, False), pos)

    def update(self):
        self.player_input()
        self.select_inventory()
        self.get_status()
        self.animate(self.status)

    def draw(self, screen):
        screen.blit(self.image, self.rect)