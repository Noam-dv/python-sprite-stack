import pygame
import sys
from sprite_stack import StackedSprite
import math
from camera import *

pygame.init()

screen = pygame.display.set_mode((500, 500), 0, 32)
display = pygame.Surface((150,150))

clock = pygame.time.Clock()

frame = 0

door = StackedSprite((25, 75), "door", 1)
crate = StackedSprite((75,75), "crate", 1)
table = StackedSprite((125,75), "table", 1)

sprs = [door, crate, table]
camera = Camera([0, 0], 1.0)

mult = 1
while True:
    display.fill((5,0,0))

    frame += 1


    for i,stack in enumerate(sprs):
        if i % 2 == 0:
            mult = -1
        else: 
            mult = 1
        stack.draw(display, frame * mult, camera)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(60)