import pygame

class Button():
    def __init__(self,
                 position: pygame.Vector2 | tuple[float, float],
                 text: str,
                 font: pygame.font.Font,
                 background_color: tuple[int, int, int] = (0, 0, 0),
                 text_color: tuple[int, int, int] = (255, 255, 255),
                 hover_background_color: tuple[int, int, int] = (0, 0, 0),
                 hover_text_color: tuple[int, int, int] = (20, 20, 0)) -> None:
        self.is_hovered: bool = False

        self.pos: pygame.Vector2 = pygame.Vector2(position)

        self.background_color: tuple[int, int, int] = background_color
        self.text_color: tuple[int, int, int] = text_color
        self.hover_text_color: tuple[int, int, int] = hover_text_color
        self.hover_background_color: tuple[int, int, int] = hover_background_color

        self.text: str = text
        self.font: pygame.font.Font = font
        self.text_surface: pygame.Surface = self.font.render(self.text, True, self.text_color, self.background_color)
        self.hover_text_surface: pygame.Surface = self.font.render(self.text, True, self.hover_text_color, self.hover_background_color)

        self.colider: pygame.Rect = self.text_surface.get_rect(topleft=self.pos)

    def draw(self, window: pygame.Surface) -> None:
        if (self.is_hovered):
            window.blit(self.hover_text_surface, self.pos)
            return

        window.blit(self.text_surface, self.pos)

    def is_clicked(self, event: pygame.event.Event) -> bool:
        return (
            event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.colider.collidepoint(event.pos)
        )
