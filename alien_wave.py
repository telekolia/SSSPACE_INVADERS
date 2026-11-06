import bullet as bullet_module
import alien as alien_module
import player
import random
import pygame
import texture_manager

class Wave:
    def __init__(self, step_size: int = 32, aliens: list[alien_module.Alien] | None = None) -> None:
        if aliens is None:
            aliens = []
        self.aliens: dict[int, alien_module.Alien] = {}
        for alien in aliens:
            self.aliens[alien.id] = alien

        self.dead_aliens: dict[str, list[pygame.Vector2]] = {}
        self.alien_bullets: list[bullet_module.Bullet] = []
        self.step_size: int = step_size
        self.step_timeout: float = 2.0
        self.step_timer: float = 0.0
        self.wave_sound: pygame.mixer.Sound = pygame.mixer.Sound('res/wave.mp3')

    def draw(self, window: pygame.Surface) -> None:
        for bullet in self.alien_bullets:
            bullet.draw(window)

        for dead_skin, dead_positions in self.dead_aliens.items():
            surface = texture_manager.TextureManager.get(dead_skin)
            surface = pygame.transform.scale_by(surface, 4.0)
            for pos in dead_positions:
                window.blit(surface, pos)

        for alien in self.aliens.values():
            alien.draw(window)

    def update(self, dt: float, player: player.Player) -> None:
        for bullet in self.alien_bullets[:]:
            if bullet.armorpiercing <= 0:
                self.alien_bullets.remove(bullet)
                continue

            if bullet.pos.x < 0 or bullet.pos.x > 960 or bullet.pos.y < 0 or bullet.pos.y > 960:
                self.alien_bullets.remove(bullet)
                continue

            bullet.update([player], dt)

        dead_alien_ids = []
        for alien in self.aliens.values():
            if alien.current_hp <= 0:
                dead_alien_ids.append(alien.id)
                player.current_score += alien.kill_points
                self.dead_aliens.setdefault(alien.dead_skin_name, []).append(alien.pos)
            else:
                if random.random() > 0.999:
                    self.alien_bullets.append(bullet_module.Bullet(alien.pos + (32, 64), 1, 1, (0, 300)))
                if alien.pos.y > 930:
                    player.current_hp = 0

        for id in dead_alien_ids:
            del self.aliens[id]

        if len(self.aliens) == 0:
            return

        self.step_timer += dt
        if self.step_timer < self.step_timeout:
            return

        self.dead_aliens.clear()
        self.step_timer = 0.0
        self.wave_sound.play()

        alien_and_position = []
        for alien in self.aliens.values():
            alien_and_position.append((alien, alien.pos))

        left_border_alien = min(alien_and_position, key=lambda e: e[1].x)[0]
        right_border_alien = max(alien_and_position, key=lambda e: e[1].x)[0]

        left_border = left_border_alien.pos.x
        right_border = right_border_alien.pos.x

        if left_border < 0 or right_border > 896:
            self.step_size *= -1
            for alien in self.aliens.values():
                alien.pos.y += 64

        for alien in self.aliens.values():
            alien.pos.x += self.step_size
            alien.hitbox.topleft = alien.pos

    def extend(self, aliens: list[alien_module.Alien]) -> None:
        for alien in aliens:
            self.aliens[alien.id] = alien
