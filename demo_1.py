import pygame
from pygame.locals import *
from sprite_stack import *
from camera import *
import sys
import os

pygame.init()
col = (0,0,0)

screen = pygame.display.set_mode((500,500), 0, 32)
display = pygame.Surface((200,200))

clock = pygame.time.Clock()

frame = 0

door = StackedSprite((25, 100), "door", 1, True)
crate = StackedSprite((75,100), "crate", 1, True)
table = StackedSprite((125,100), "table", 1, True)

sprs = [door, crate, table]

camera = Camera([0, 0], 1.0)

key_a_held = False
key_d_held = False

font = pygame.font.Font(None,24)
lines = ['try pressing A and D and moving your mouse', 'to the edges of the screen :-)']

rendered_lines = [font.render(line, True, (255, 255, 255)) for line in lines]

while True:
    display.fill((5,0,0))

    frame += 1
    if key_a_held:
        camera.offset_angle(-2)
    if key_d_held:
        camera.offset_angle(2)
    camera.move_towards_edge(screen.get_size())

    for stack in sprs:
        stack.draw(display, camera.angle, camera)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                key_a_held = True
            if event.key == K_d:
                key_d_held = True
        if event.type == KEYUP:
            if event.key == K_a:
                key_a_held = False
            if event.key == K_d:
                key_d_held = False

    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))

    for i, rendered_line in enumerate(rendered_lines):
        screen.blit(rendered_line, (10, 10 + i * 20))

    pygame.display.update()
    clock.tick(60)
