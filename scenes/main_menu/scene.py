import pygame
import ui_components.simple_text_button as simple_text_button

class MainMenu():
    game_title = "SSSPACE INVADERS"
    litle_author_note = "by teleko"

    def __init__(self, window: pygame.Surface) -> None:
        self.window: pygame.Surface = window
        self.center_x: int = self.window.get_rect().centerx
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.big_font: pygame.font.Font = pygame.font.Font("res/fonts/PixelifySans-VariableFont_wght.ttf", 32)
        self.small_font: pygame.font.Font = pygame.font.Font("res/fonts/PixelifySans-VariableFont_wght.ttf", 24)

        self.game_title_image: pygame.Surface = self.big_font.render(self.game_title, True, (255, 255, 255))
        self.author_note_image: pygame.Surface = self.small_font.render(self.litle_author_note, True, (255, 255, 255))

        self.start_button: simple_text_button.Button = simple_text_button.Button((self.center_x, 64 * 3), "Start", self.small_font)
        self.start_button.pos.x -= self.start_button.text_surface.get_width() / 2
        self.start_button.colider.topleft = self.start_button.pos
        self.exit_button: simple_text_button.Button = simple_text_button.Button((self.center_x, 64 * 4), "Exit", self.small_font)
        self.exit_button.pos.x -= self.exit_button.text_surface.get_width() / 2
        self.exit_button.colider.topleft = self.exit_button.pos

    def draw(self) -> None:
        self.window.fill((0, 0, 0))
        self.window.blit(self.game_title_image, self.game_title_image.get_rect(midtop=(self.center_x, 64)))
        self.window.blit(self.author_note_image, self.author_note_image.get_rect(midtop=(self.center_x, 64 * 2)))

        self.start_button.draw(self.window)
        self.exit_button.draw(self.window)

    def start_scene(self) -> int:
        while True:
            self.clock.tick(60)
            for single_event in pygame.event.get():
                if (single_event.type == pygame.QUIT):
                    return 1
                if (self.start_button.is_clicked(single_event)):
                    return 0
                if (self.exit_button.is_clicked(single_event)):
                    return 1
                if (single_event.type == pygame.KEYDOWN and single_event.key == pygame.K_ESCAPE):
                    return 1

            self.start_button.is_hovered = self.start_button.colider.collidepoint(pygame.mouse.get_pos())
            self.exit_button.is_hovered = self.exit_button.colider.collidepoint(pygame.mouse.get_pos())
            self.draw()
            pygame.display.update()
