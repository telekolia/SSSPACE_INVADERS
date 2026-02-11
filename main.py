import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF, RESIZABLE
from texture_manager import TextureManager
from player import Player

player = Player()

TextureManager.load_directory('res')

pygame.init()
window = pygame.display.set_mode((64 * 15, 64 * 15), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("Симуляция жизни")
pygame.display.set_icon(TextureManager.get("player"))

clock = pygame.time.Clock()
game_timer = 0.0
dt = 0.0

background = pygame.Rect(0, 0, 1920, 1080)

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

    pygame.draw.rect(window, (0, 0, 0), background)
    player.proccess_event(dt)
    player.draw(window)
    pygame.display.update()

    dt = clock.tick(60) / 1000.0
    # Update
    game_timer += dt

pygame.quit()
