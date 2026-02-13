from alien import Alien
from alien_wave import Wave
import random
from pygame.math import Vector2

class WaveManager:
    def __init__(self):
        self.waves = []
        # self.aliens = []

    def update(self, dt):
        for wave in self.waves[:]:
            if len(wave.aliens) == 0:
                self.waves.remove(wave)

        if len(self.waves) == 0:
            number_of_waves = random.randint(3, 8)
            for h in range(number_of_waves):
                if random.random() > 0.7:
                    aliens_collection = [Alien((0,0), 1) for _ in range(5)] # easy_wave
                else:
                    aliens_collection = [Alien((0,0), i) for _ in range(4) for i in range(1, 2)] # difficult_wave

                possible_positions = [(i, 0) for i in range(0, 10*64, 64)]
                random.shuffle(possible_positions)
                for alien in aliens_collection:
                    alien.pos = Vector2(possible_positions.pop())
                    alien.pos.y = h * 64

                # self.aliens.extend(aliens_collection)
                self.waves.append(Wave(50, aliens_collection))

        for wave in self.waves:
            wave.update(dt)

    def draw(self, window):
        if len(self.waves) == 0:
            return

        for wave in self.waves:
            wave.draw(window)

    @property
    def aliens(self):
        aliens = []
        if len(self.waves) == 0:
            return aliens

        for wave in self.waves:
            aliens.extend(wave.aliens.values())

        return aliens
