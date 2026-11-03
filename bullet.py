from __future__ import annotations

import collections.abc
import typing
import pygame
import texture_manager

if typing.TYPE_CHECKING:
    import alien
    import player

class Bullet:
    def __init__(self, pos: pygame.Vector2 | tuple[float, float], damage: int, armorpiercing: int, speed: pygame.Vector2 | tuple[float, float]) -> None:
        self.pos: pygame.Vector2 = pygame.Vector2(pos)
        self.texture_name: str = "bullet"
        self.hitbox: pygame.Rect = pygame.Rect(self.pos, (8, 16))
        self.damage: int = damage
        self.armorpiercing: int = armorpiercing
        self.speed: pygame.Vector2 = pygame.Vector2(speed)
        self.bullet_surface = texture_manager.TextureManager.get(self.texture_name)
        self.bullet_surface = pygame.transform.scale_by(self.bullet_surface, 4.0)

    def update(self, targets: collections.abc.Iterable[alien.Alien | player.Player], dt: float) -> None:
        for target in targets:
            if self.hitbox.colliderect(target.hitbox):
                target.current_hp -= self.damage
                self.armorpiercing -= 1

        self.pos += self.speed * dt
        self.hitbox.topleft = self.pos

    def draw(self, window: pygame.Surface) -> None:
        angle = self.speed.as_polar()[1]
        self.bullet_surface = pygame.transform.rotate(self.bullet_surface, -angle - 90)
        bullet_rect = self.bullet_surface.get_rect(center=self.hitbox.center)
        window.blit(self.bullet_surface, self.pos)
