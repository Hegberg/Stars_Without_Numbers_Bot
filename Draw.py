import pygame

import Colour

class Pygame_Object(object):
    
    def __init__(self, x, y):
        self.game_display = None
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()

        self.pygame_init()

        self.ui_text = pygame.font.Font('freesansbold.ttf',20)
        

    def pygame_init(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Faction Visualizer")

        pass

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            #print(event)

        pygame.display.update()
        self.clock.tick(60)

        return 0

    def draw_polygon(self, colour, points):
        pygame.draw.polygon(self.game_display, colour, points)
        return

    def draw_rectangle(self, colour, points):
        pygame.draw.rect(self.game_display, colour, points)


    def draw_ui_buttons(self):
        self.draw_end_turn(Colour.white)

    def draw_end_turn(self, colour):
        rec_location = [(0,self.y - 50), (100, self.y)]
        self.draw_rectangle(colour, rec_location)

        text_surface = self.ui_text.render("End Turn", False, (0, 0, 0))
        center = (rec_location[0][0] + 5, rec_location[0][1] + 15)
        self.game_display.blit(text_surface, center)