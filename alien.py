import pygame
from pygame.math import Vector2
from texture_manager import TextureManager

class Alien:
    last_id = 0

    def __init__(self, pos: Vector2, max_hp=1):
        self.id = Alien.last_id + 1
        self.pos = Vector2(pos)
        self.hitbox = pygame.Rect(self.pos, (64, 64))
        self.skin_name = "alien"
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.bullets = []

    def draw(self, window):
        texture = TextureManager.get(self.skin_name)
        window.blit(texture, self.pos)
