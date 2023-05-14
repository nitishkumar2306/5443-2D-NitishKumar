from pygame import Vector2

from Level.Level import Level
from objects.Enemy.Enemy3 import Enemy3
from objects.GameObject import GameObject
from objects.Wall.MovingWall import MovingWall
from objects.Wall.Wall import Wall
from objects.collectable.Bullets import Bullets
from utils.assets_manager import assetsManager
from pytmx import load_pygame, TiledTileLayer

from utils.util import utils


class Level6(Level):
    def __init__(self):
        # Getting / Importing the map
        self.tmxdata = load_pygame("assets/6.tmx")
        self.width = self.tmxdata.width * self.tmxdata.tilewidth
        self.height = self.tmxdata.height * self.tmxdata.tileheight

        self.tileSize = Vector2(16, 16)

        self.ti = self.tmxdata.get_tile_image_by_gid

        self.gameObjects = []

        self.bg = GameObject(Vector2(0,0),assetsManager.get("bg"))

        rows, cols = (100, 50)
        utils.grid = [[0 for x in range(cols)] for y in range(rows)]

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, TiledTileLayer) and layer.name == 'wall':
                for x, y, gid, in layer:
                    tile = self.ti(gid)
                    if tile:
                        image = self.tmxdata.get_tile_image_by_gid(gid)
                        posX = x * self.tileSize.x
                        posY = y * self.tileSize.y
                        self.gameObjects.append(Wall( Vector2(posX,posY),assetsManager.get("wall"),False))


        self.playerPos = Vector2(0, 450)
        self.gameObjects.append(Enemy3(Vector2(8 * 16,8* 16),Vector2(66*16,8*16),self.gameObjects.append))
        self.gameObjects.append(Bullets(Vector2(18 * 16,24*16)))
        self.gameObjects.append(Bullets(Vector2(23 * 16, 24 * 16)))
        self.gameObjects.append(Bullets(Vector2(25 * 16, 24 * 16)))
        self.gameObjects.append(Bullets(Vector2(28 * 16, 24 * 16)))
        self.gameObjects.append(Bullets(Vector2(32 * 16, 24 * 16)))
        self.gameObjects.append(Bullets(Vector2(38 * 16, 24 * 16)))

    def draw(self):
        self.bg.pos = Vector2(0,0)
        self.bg.draw()
        self.bg.pos = Vector2(800, 0)
        self.bg.draw()

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, TiledTileLayer) and layer.visible:
                for x, y, gid, in layer:
                    tile = self.ti(gid)
                    if tile:
                        image = self.tmxdata.get_tile_image_by_gid(gid)
                        posX = x * self.tileSize.x
                        posY = y * self.tileSize.y
                        utils.screen.blit(image, (posX - utils.camera.x, posY - utils.camera.y))
