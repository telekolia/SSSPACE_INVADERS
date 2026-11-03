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

    def update(self, targets: collections.abc.Iterable[alien.Alien | player.Player], dt: float) -> None:
        for target in targets:
            if self.hitbox.colliderect(target.hitbox):
                target.current_hp -= self.damage
                self.armorpiercing -= 1

        self.pos += self.speed * dt
        self.hitbox.topleft = self.pos

    def draw(self, window: pygame.Surface) -> None:
        texture = texture_manager.TextureManager.get(self.texture_name)
        angle = self.speed.as_polar()[1]
        texture = pygame.transform.rotate(texture, -angle - 90)
        texture_rect = texture.get_rect(center=self.hitbox.center)
        window.blit(texture, self.pos)
