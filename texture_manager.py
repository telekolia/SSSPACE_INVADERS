import pygame
import pathlib

class TextureManager:
    textures: dict[str, pygame.Surface] = {}

    @classmethod
    def load_directory(cls, directory_path: str | pathlib.Path, recursive: bool = True) -> None:
        path = pathlib.Path(directory_path)

        if recursive:
            files = path.rglob("*.png")
        else:
            files = path.glob("*.png")

        for file_path in files:
            texture_name = file_path.stem
            try:
                texture = pygame.image.load(str(file_path))
                TextureManager.textures[texture_name] = texture
                print(f"Loaded texture: {texture_name}")
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")

    @classmethod
    def get(cls, texture_name: str) -> pygame.Surface:
        return TextureManager.textures[texture_name]
