from alien import Alien
from alien_wave import Wave
import random
from pygame.math import Vector2

class WaveManager:
    def __init__(self):
        self.wave = Wave(16)

    def update(self, dt):
        if len(self.wave.aliens) == 0:
            for h in range(5):
                if h % 2 == 0:
                    aliens_collection = [Alien((0,0), 1, "a") for _ in range(12)] # easy_wave
                else:
                    aliens_collection = [Alien((0,0), 2, "b") for _ in range(12)] # difficult_wave

                possible_positions = [(i, 0) for i in range(128, 896, 66)]
                random.shuffle(possible_positions)
                for alien in aliens_collection:
                    alien.pos = Vector2(possible_positions.pop())
                    alien.pos.y = (h + 2) * 64

                self.wave.extend(aliens_collection)

        new_step_timeout = 1.0 * len(self.wave.aliens) / 60.0
        self.wave.step_timeout = new_step_timeout
        self.wave.update(dt)

    def draw(self, window):
            self.wave.draw(window)

    @property
    def aliens(self):
        aliens = []
        if len(self.wave.aliens) == 0:
            return aliens

        aliens.extend(self.wave.aliens.values())

        return aliens
