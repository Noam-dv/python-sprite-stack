import pygame

class Camera:
    def __init__(self, pos, zoom):
        self.scroll_factor = list(pos)
        self.zoom = zoom
        self.angle = 0

    def offset_angle(self, diff):
        self.angle += diff

    def move_towards_edge(self, window_size, speed=1):
        mx, my = pygame.mouse.get_pos()
        edge_margin = 50
        if mx < edge_margin:
            self.scroll_factor[0] -= speed
        elif mx > window_size[0] - edge_margin:
            self.scroll_factor[0] += speed
        if my < edge_margin:
            self.scroll_factor[1] -= speed
        elif my > window_size[1] - edge_margin:
            self.scroll_factor[1] += speed