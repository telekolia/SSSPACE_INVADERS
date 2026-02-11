import pygame
from pygame.math import Vector2

class Wave:
    def __init__(self, speed, aliens=[]):
        self.aliens = {}
        for alien in aliens:
            self.aliens[alien.id] = alien
        self.speed = speed

    def draw(self, window):
        for alien in self.aliens.values():
            alien.draw(window)

    def update(self, dt):
        dead_alien_ids = []
        for alien in self.aliens.values():
            if alien.current_hp <= 0:
                dead_alien_ids.append(alien.id)

        for id in dead_alien_ids:
            del self.aliens[id]

        alien_and_position = []
        for alien in self.aliens.values():
            alien_and_position.append((alien, alien.pos))

        left_border_alien = min(alien_and_position, key=lambda e: e[1].x)[0]
        right_border_alien = max(alien_and_position, key=lambda e: e[1].x)[0]

        left_border = left_border_alien.pos.x
        right_border = right_border_alien.pos.x

        if left_border <= 0 or right_border > 896:
            self.speed *= -1
            for alien in self.aliens.values():
                alien.pos.y += 64


        for alien in self.aliens.values():
            alien.pos.x += self.speed * dt
