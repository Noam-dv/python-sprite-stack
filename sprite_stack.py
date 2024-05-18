import pygame
from pygame.locals import *
import sys
import os
import math

class StackedSprite:
    def __init__(self, world_pos, packer_folder, height, customize_depth=False):
        self.packer_folder = packer_folder
        self.height = height
        self.world_pos = world_pos
        self.sprites = []
        self.cache = {} # will add caching for every generated angle, so pygame doesnt need to rerender all the frames
        self.customize_depth = customize_depth

        self.init_graphics()

    def draw(self, surf, rot, camera):
        for i, s in enumerate(self.sprites):
            spr = pygame.transform.rotate(s, rot)
            pos = self.fixed_pos(spr, i)
            if self.customize_depth:
                pos = self.fixed_pos_depth(spr, i, camera)
            surf.blit(spr, pos)

    def fixed_pos(self, spr, index):
        return self.world_pos[0]-spr.get_width() // 2, self.world_pos[1] - spr.get_height() // 2 - index * self.height

    def fixed_pos_depth(self, spr, index, camera):
        depth_factor = -0.005 
        depth_offset = index * self.height * depth_factor
        x = self.world_pos[0] - camera.scroll_factor[0] - spr.get_width() // 2
        y = self.world_pos[1] - camera.scroll_factor[1] - spr.get_height() // 2 - depth_offset

        angle_rad = math.radians(camera.angle)
        scale = 1.0 - depth_offset * math.cos(angle_rad)
        x = camera.scroll_factor[0] + (x - camera.scroll_factor[0]) * scale
        y = camera.scroll_factor[1] + (y - camera.scroll_factor[1]) * scale

        y += depth_offset * math.sin(angle_rad)

        return x, y

    def init_graphics(self):
        for i in os.listdir(self.packer_folder):
            sprite_path = os.path.join(self.packer_folder, i)
            try:
                sprite_image = pygame.image.load(sprite_path)
                self.sprites.append(sprite_image)
                print(f"loaded {sprite_path}")
            except pygame.error as e:
                print(f"failde to load {sprite_path}: {e}")
        print(self.sprites)