import pygame
from pygame.math import Vector2
from texture_manager import TextureManager
from math import atan

class Bullet:
    def __init__(self, pos: Vector2, damage, armorpiercing, speed: Vector2):
        self.pos = Vector2(pos)
        self.texture_name = "bullet"
        self.hitbox = pygame.Rect(self.pos, (8, 16))
        self.damage = damage
        self.armorpiercing = armorpiercing
        self.speed = Vector2(speed)

    def update(self, aliens, dt):
        for alien in aliens:
            if self.hitbox.colliderect(alien.hitbox):
                alien.current_hp -= self.damage
                self.armorpiercing -= 1

        self.pos += self.speed * dt
        self.hitbox.topleft = self.pos

    def draw(self, window):
        texture = TextureManager.get(self.texture_name)
        angle = self.speed.as_polar()[1]
        pygame.transform.rotate(texture, -angle)
        window.blit(texture, self.pos)


class Player:
    def __init__(self):
        self.pos = Vector2((64*7, 64*13))
        self.hitbox = pygame.Rect(self.pos, (64, 64))
        self.skin_name = "player"
        self.speed = 32
        self.max_hp = 3
        self.current_hp = 3
        self.bullets = []
        self.fire_timeout = 0.3 # seconds
        self.fire_timer = 0.0
        self.move_timer = 0.0
        self.move_timeout = 0.2

    def proccess_event(self, dt, aliens):
        keys = pygame.key.get_pressed()

        self.move_timer += dt
        if self.move_timer >= self.move_timeout:
            # Движение вверх (a, LEFT)
            if self.pos.x > 0:
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    self.move_timer = 0.0
                    self.pos.x -= self.speed

            # Движение вправо (d, RIGHT)
            if self.pos.x < 896:
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    self.move_timer = 0.0
                    self.pos.x += self.speed

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.fire(dt)

        for bullet in self.bullets[:]:
            if bullet.armorpiercing <= 0:
                self.bullets.remove(bullet)
                continue

            if bullet.pos.x < 0 or bullet.pos.x > 944 or bullet.pos.y < 0 or bullet.pos.y > 960:
                self.bullets.remove(bullet)
                continue

            bullet.update(aliens, dt)

    def draw(self, window):
        texture = TextureManager.get(self.skin_name)
        window.blit(texture, self.pos)

        for bullet in self.bullets:
            bullet.draw(window)

    def fire(self, dt):
        self.fire_timer += dt
        if self.fire_timer >= self.fire_timeout:
            self.fire_timer = 0.0
            self.bullets.append(Bullet(self.pos + Vector2(28, 0), 1, 1, (0, -500)))
