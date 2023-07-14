import pygame, random

# class Particle(pygame.sprite.Sprite):
#     def __init__(self, screen, x, y, radius, color):
#         super().__init__()
#         self.screen = screen
#         self.x = x
#         self.y = y
#         self.radius = radius
#         self.color = color

#     def draw(self):
#         pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)


class ParticlePrinciple:
    def __init__(self, screen, offset):
        self.particles = []
        self.screen = screen
        self.offset = offset

    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.1
                pygame.draw.circle(self.screen, (255, 0, 0), particle[0] - self.offset, int(particle[1]))

    def add_particles(self):
        pos_x = 250
        pos_y = 250
        radius = 10
        direction_x = random.randint(-4, 4)
        direction_y = random.randint(-4, 4)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]


        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy