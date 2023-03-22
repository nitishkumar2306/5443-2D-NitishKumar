import math

import pygame
from pygame import Vector2

from objects.gameObject import GameObject
from utils.SpriteSheet import SpriteSheet
from utils.assets_manager import assetsManager
from utils.util import utils


class Explosion(GameObject):
    def __init__(self, pos):
        self.animSheet = SpriteSheet(assetsManager.get("explo1"), 1, 12)
        self.animSheet.setPlay(0, 11, 0.1, False)
        super().__init__(pos, self.animSheet.getCurrentFrame(), "explo")

    def update(self):
        super().update()
        self.animSheet.play()

    def draw(self):
        self.img = self.animSheet.getCurrentFrame()
        super().draw()
