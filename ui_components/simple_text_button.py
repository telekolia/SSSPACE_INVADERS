from pygame import Vector2, MOUSEBUTTONDOWN
from pygame.surface import Surface
from pygame.font import Font
from pygame.event import Event

class Button():
    def __init__(self,
                 position: Vector2,
                 text: str,
                 font: Font,
                 background_color = (0, 0, 0),
                 text_color = (255, 255, 255),
                 hover_background_color = (0, 0, 0),
                 hover_text_color = (20, 20, 0)):
        self.is_hovered = False

        self.pos = Vector2(position)

        self.background_color = background_color
        self.text_color = text_color
        self.hover_text_color = hover_text_color
        self.hover_background_color = hover_background_color

        self.text = text
        self.font = font
        self.text_surface = self.font.render(self.text, True, self.text_color, self.background_color)
        self.hover_text_surface = self.font.render(self.text, True, self.hover_text_color, self.hover_background_color)

        self.colider = self.text_surface.get_rect(topleft=self.pos)

    def draw(self, window: Surface) -> None:
        if (self.is_hovered):
            window.blit(self.hover_text_surface, self.pos)
            return

        window.blit(self.text_surface, self.pos)

    def is_clicked(self, event: Event):
        return (
            event.type == MOUSEBUTTONDOWN
            and event.button == 1
            and self.colider.collidepoint(event.pos)
        )
