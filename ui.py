import pygame
import texture_manager

player_name_title = "Player: "

class UI:
    def __init__(self) -> None:
        self.hp_bar_pos: pygame.Vector2 = pygame.Vector2(0, 64)
        self.hp_amount: int = 3
        self.player_name_pos: pygame.Vector2 = pygame.Vector2()
        self.player_name: str = "Not stated"
        self.score: int = 1000
        self.score_pos: pygame.Vector2 = pygame.Vector2()
        self.font: pygame.font.Font = pygame.font.Font("res/fonts/PixelifySans-VariableFont_wght.ttf", 32)

        heart_texture = texture_manager.TextureManager.get("player")
        self.heart_surface: pygame.Surface = pygame.transform.scale_by(heart_texture, 4.0)

    def draw(self, window: pygame.Surface) -> None:
        if (self.hp_amount > 0):
            for i in range(self.hp_amount):
                next_heart_pos = self.hp_bar_pos + (i * 80, 0)
                window.blit(self.heart_surface, next_heart_pos)

        player_name_image = self.font.render(player_name_title + "[" + self.player_name + "]", True, (255, 255, 255))
        window.blit(player_name_image, self.player_name_pos)

        score_image = self.font.render(str(self.score)[:-3] + "." + str(self.score)[-3:], True, (255, 255, 255))
        window.blit(score_image, self.score_pos)
