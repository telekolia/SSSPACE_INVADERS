import pygame
import texture_manager
import random
import alien
import bullet

class Player:
    def __init__(self) -> None:
        self.pos: pygame.Vector2 = pygame.Vector2((64*7, 64*13))
        self.hitbox: pygame.Rect = pygame.Rect(self.pos, (64, 64))
        self.skin_name: str = "player"

        self.speed: int = 32
        self.max_hp: int = 3
        self.current_hp: int = 3

        self.current_score = 0

        self.bullets: list[bullet.Bullet] = []
        self.fire_timeout: float = 0.3 # seconds
        self.fire_timer: float = 0.0
        self.move_timer: float = 0.0
        self.move_timeout: float = 0.2
        self.fire_sounds: list[pygame.mixer.Sound] = [pygame.mixer.Sound('res/fire1.ogg'), pygame.mixer.Sound('res/fire2.ogg'), pygame.mixer.Sound('res/fire3.ogg')]
        for sound in self.fire_sounds:
            sound.set_volume(0.4)

    def proccess_event(self, dt: float, aliens: list[alien.Alien]) -> None:
        keys = pygame.key.get_pressed()

        self.move_timer += dt
        self.fire_timer += dt
        if self.move_timer >= self.move_timeout:
            # Движение вверх (a, LEFT)
            if self.pos.x > 0:
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    self.move_timer = 0.0
                    self.pos.x -= self.speed

            # Движение вправо (d, RIGHT)
            if self.pos.x < 896:
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    self.move_timer = 0.0
                    self.pos.x += self.speed

            self.hitbox.topleft = self.pos

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.fire(dt)

        for bullet in self.bullets[:]:
            if bullet.armorpiercing <= 0:
                self.bullets.remove(bullet)
                continue

            if bullet.pos.x < 0 or bullet.pos.x > 944 or bullet.pos.y < 0 or bullet.pos.y > 960:
                self.bullets.remove(bullet)
                continue

            bullet.update(aliens, dt)

    def draw(self, window: pygame.surface.Surface) -> None:
        texture = texture_manager.TextureManager.get(self.skin_name)
        texture = pygame.transform.scale_by(texture, 4.0)
        window.blit(texture, self.pos)

        for bullet in self.bullets:
            bullet.draw(window)

    def fire(self, dt: float) -> None:
        # if self.fire_timer >= self.fire_timeout:
        if len(self.bullets) == 0:
            self.fire_timer = 0.0
            self.bullets.append(bullet.Bullet(self.pos + pygame.Vector2(28, 0), 1, 1, (0, -500)))

            random.shuffle(self.fire_sounds)
            self.fire_sounds[0].play()
