from player import Player
from wave_manager import WaveManager
from ui import UI
import pygame

class AlienWave():
    def __init__(self, window: pygame.Surface):
        self.window = window

        self.ui = UI()
        self.ui.player_name_pos = pygame.Vector2(0, 0)
        self.ui.score_pos = pygame.Vector2(64 * 7, 0)
        self.ui.hp_bar_pos = pygame.Vector2(0, 64)

        self.clock = pygame.time.Clock()
        self.game_timer = 0.0
        self.dt = 0.0

        self.player = Player()
        self.wave_manager = WaveManager()

    def draw(self) -> None:
        self.window.fill((0, 0, 0))
        self.wave_manager.draw(self.window)
        self.player.draw(self.window)
        self.ui.draw(self.window)

    def startScene(self) -> int:
        while True:
            self.dt = self.clock.tick(60) / 1000.0

            for single_event in pygame.event.get():
                if (single_event.type == pygame.QUIT):
                    return 0
                if (single_event.type == pygame.KEYDOWN and single_event.key == pygame.K_ESCAPE):
                    return 0

            self.player.proccess_event(self.dt, self.wave_manager.aliens)
            self.wave_manager.update(self.dt)
            self.ui.hp_amount = self.player.current_hp

            if (self.player.current_hp <= 0):
                return 0

            self.draw()
            pygame.display.update()
            self.game_timer += self.dt
