import pygame
import texture_manager
import bullet

class Alien:
    last_id: int = 0

    def __init__(self, pos: pygame.Vector2 | tuple[float, float], max_hp: int = 1, skin_name: str = "a") -> None:
        Alien.last_id += 1
        self.id: int = Alien.last_id
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        self.hitbox: pygame.Rect = pygame.Rect(self.pos, (64, 64))
        self.skin_name: str = skin_name
        self.dead_skin_name: str = "a_dead"
        self.max_hp: int = max_hp
        self.current_hp: int = max_hp
        self.bullets: list[bullet.Bullet] = []
        self.kill_points: int = 100

    def draw(self, window: pygame.Surface) -> None:
        texture = texture_manager.TextureManager.get(self.skin_name)
        texture = pygame.transform.scale_by(texture, 4.0)
        window.blit(texture, self.pos)
