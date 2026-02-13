import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE
from texture_manager import TextureManager
from player import Player, Bullet
from wave_manager import WaveManager

player = Player()
wave_manager = WaveManager()

TextureManager.load_directory('res')

pygame.init()
window = pygame.display.set_mode((64 * 15, 64 * 15), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("SSSPACE INVADERS!")
pygame.display.set_icon(TextureManager.get("player"))

clock = pygame.time.Clock()
game_timer = 0.0
dt = 0.0

running = True
while running:
    # Handle input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                break

    player.proccess_event(dt, wave_manager.aliens)
    wave_manager.update(dt)

    window.fill((0, 0, 0))
    wave_manager.draw(window)
    player.draw(window)
    pygame.display.update()

    dt = clock.tick(60) / 1000.0
    # Update
    game_timer += dt

pygame.quit()
