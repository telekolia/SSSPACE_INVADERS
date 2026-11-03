import pygame
import texture_manager
import scenes.main_menu.scene as main_menu_scene
import scenes.alien_wave.scene as alien_wave_scene

texture_manager.TextureManager.load_directory('res')

pygame.init()
window = pygame.display.set_mode((64 * 15, 64 * 15), pygame.HWSURFACE | pygame.DOUBLEBUF)
pygame.display.set_caption("SSSPACE INVADERS!")
pygame.display.set_icon(texture_manager.TextureManager.get("player"))

pygame.mixer.init()
pygame.mixer.set_num_channels(32)

main_menu = main_menu_scene.MainMenu(window)

while True:
    result = main_menu.start_scene()
    if (result == 1):
        break
    if (result == 0):
        game_scene = alien_wave_scene.AlienWave(window)
        game_scene.start_scene()
        pygame.mixer.stop()

pygame.quit()
