import pygame

pygame.init()
class CameraGroup(pygame.sprite.Group):
    def __init__(self, mapa, x, y, extra_group = None):
        super().__init__()
        self.mapa = mapa
        self.x = x
        self.y = y
        self.display_surface = pygame.display.get_surface()
        self.extra_group = extra_group

        self.offset = pygame.math.Vector2(0,0)
        

        self.half_w = self.display_surface.get_size()[0] / 2
        self.half_h = self.display_surface.get_size()[1] / 2

        # Zoom
        self.zoom_scale = 1.75
        self.internal_surface_size = (self.display_surface.get_width(), self.display_surface.get_height())
        self.internal_surface = pygame.Surface(self.internal_surface_size, pygame.SRCALPHA)
        self.internal_surface_rect = self.internal_surface.get_rect(center = (self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(self.internal_surface_size)

        self.mapa_rect = self.mapa.get_rect(topleft=(self.x, self.y))

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def returnOffset(self):
        return self.offset



    def custom_draw(self, player):

        self.center_target_camera(player)

        self.internal_surface.fill((48, 44, 46))


        ground_offset = self.mapa_rect.topleft - self.offset
        self.internal_surface.blit(self.mapa, ground_offset)

        if self.extra_group != None:
            for sprite in self.extra_group.sprites():
                offset_pos = sprite.rect.topleft - self.offset
                self.internal_surface.blit(sprite.image, offset_pos)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.bottom):
            offset_pos = sprite.rect.topleft - self.offset
            self.internal_surface.blit(sprite.image, offset_pos)


        scaled_surf = pygame.transform.scale(self.internal_surface, (int(self.internal_surface_size_vector.x * self.zoom_scale), int(self.internal_surface_size_vector.y * self.zoom_scale)))
        scaled_rect = scaled_surf.get_rect(center = (self.half_w, self.half_h))

        self.display_surface.blit(scaled_surf, scaled_rect)
    
    def draw(self):
        self.display_surface.blit(self.mapa, (self.x, self.y))

        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)