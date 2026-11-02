from pygame.math import Vector2
from pygame.surface import Surface
from pygame.font import Font
from pygame.transform import scale_by
from texture_manager import TextureManager

player_name_title = "Player: "

class UI:
    def __init__(self):
        self.hp_bar_pos = Vector2(0, 64)
        self.hp_amount = 3
        self.player_name_pos = Vector2()
        self.player_name = "Not stated"
        self.score = 1000
        self.score_pos = Vector2()
        self.font = Font(None, 16)

        heart_texture = TextureManager.get("heart")
        self.heart_surface = scale_by(heart_texture, 4.0)

    def draw(self, window: Surface) -> None:
        if (self.hp_amount > 0):
            for i in range(self.hp_amount):
                next_heart_pos = self.hp_bar_pos + (i * 80, 0)
                window.blit(self.heart_surface, next_heart_pos)

        player_name_image = self.font.render(player_name_title + "[" + self.player_name + "]", True, (255, 255, 255))
        player_name_image = scale_by(player_name_image, 4.0)
        window.blit(player_name_image, self.player_name_pos)

        score_image = self.font.render(str(self.score)[:-3] + "." + str(self.score)[-3:], True, (255, 255, 255))
        score_image = scale_by(score_image, 4.0)
        window.blit(score_image, self.score_pos)
