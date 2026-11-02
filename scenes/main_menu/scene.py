from pygame.surface import Surface
from pygame.font import Font
from pygame import event, mouse, display, time, QUIT, KEYDOWN, K_ESCAPE
from ui_components.simple_text_button import Button

class MainMenu():
    game_title = "SSSPACE INVADERS"
    litle_author_note = "by teleko"

    def __init__(self, window: Surface):
        self.window = window
        self.center_x = self.window.get_rect().centerx
        self.clock = time.Clock()
        self.big_font = Font("res/fonts/PixelifySans-VariableFont_wght.ttf", 32)
        self.small_font = Font("res/fonts/PixelifySans-VariableFont_wght.ttf", 24)

        self.game_title_image = self.big_font.render(self.game_title, True, (255, 255, 255))
        self.author_note_image = self.small_font.render(self.litle_author_note, True, (255, 255, 255))

        self.start_button = Button((self.center_x, 64 * 3), "Start", self.small_font)
        self.start_button.pos.x -= self.start_button.text_surface.get_width() / 2
        self.start_button.colider.topleft = self.start_button.pos
        self.exit_button = Button((self.center_x, 64 * 4), "Exit", self.small_font)
        self.exit_button.pos.x -= self.exit_button.text_surface.get_width() / 2
        self.exit_button.colider.topleft = self.exit_button.pos

    def draw(self) -> None:
        self.window.fill((0, 0, 0))
        self.window.blit(self.game_title_image, self.game_title_image.get_rect(midtop=(self.center_x, 64)))
        self.window.blit(self.author_note_image, self.author_note_image.get_rect(midtop=(self.center_x, 64 * 2)))

        self.start_button.draw(self.window)
        self.exit_button.draw(self.window)

    def startScene(self) -> int:
        while True:
            self.clock.tick(60)
            for single_event in event.get():
                if (single_event.type == QUIT):
                    return 1
                if (self.start_button.is_clicked(single_event)):
                    return 0
                if (self.exit_button.is_clicked(single_event)):
                    return 1
                if (single_event.type == KEYDOWN and single_event.key == K_ESCAPE):
                    return 1

            self.start_button.is_hovered = self.start_button.colider.collidepoint(mouse.get_pos())
            self.exit_button.is_hovered = self.exit_button.colider.collidepoint(mouse.get_pos())
            self.draw()
            display.update()
