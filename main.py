import pygame
from pygame.constants import HWSURFACE, DOUBLEBUF
from texture_manager import TextureManager
from scenes.main_menu.scene import MainMenu
from scenes.alien_wave.scene import AlienWave

TextureManager.load_directory('res')

pygame.init()
window = pygame.display.set_mode((64 * 15, 64 * 15), HWSURFACE | DOUBLEBUF)
pygame.display.set_caption("SSSPACE INVADERS!")
pygame.display.set_icon(TextureManager.get("player"))

pygame.mixer.init()
pygame.mixer.set_num_channels(32)

main_menu = MainMenu(window)

while True:
    result = main_menu.startScene()
    if (result == 1):
        break
    if (result == 0):
        game_scene = AlienWave(window)
        game_scene.startScene()
        pygame.mixer.stop()

pygame.quit()
