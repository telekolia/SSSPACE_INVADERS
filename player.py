import pygame
from pygame.math import Vector2
from texture_manager import TextureManager

class Bullet:
    def __init__(self, pos: Vector2, damage, armorpiercing, speed: Vector2):
        self.pos = Vector2(pos)
        self.damage = damage
        self.armorpiercing = armorpiercing
        self.speed = Vector2(speed)

    def update(self, enimies):
        for enimy in enimies:
            if self.pos.x >= enimy.pos.x &
               self.pos.x < enimy.pos.y


class Player:
    def __init__(self):
        self.pos = Vector2((64*7, 64*13))
        self.skin_name = "player"
        self.speed = 200
        self.max_hp = 3
        self.current_hp = 3
        self.bullets = []

    def proccess_event(self, dt):
        keys = pygame.key.get_pressed()

        # Движение вверх (a, LEFT)
        if self.pos.x > 0:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.pos.x -= self.speed * dt

        # Движение вправо (d, RIGHT)
        if self.pos.x < 896:
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.pos.x += self.speed * dt

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            pass

    def draw(self, window):
        texture = TextureManager.get(self.skin_name)
        window.blit(texture, self.pos)
