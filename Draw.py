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

        self.end_turn_location = [(0,self.y - 50), (100, self.y)]#top left point, bottom right point

        self.mouse_down = False;

        self.amount_of_ui_elements = 1
        self.ui_element_clicked = [0] * self.amount_of_ui_elements

        
        

    def pygame_init(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Faction Visualizer")

        pass

    def update(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                self.check_where_mouse_clicked(pos)
                self.mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
                for i in range(0, self.amount_of_ui_elements):
                    self.ui_element_clicked[i] = 0
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
        if (self.ui_element_clicked[0]):
            self.draw_end_turn(Colour.gray)
        else:
            self.draw_end_turn(Colour.white)

    def draw_end_turn(self, colour):
        self.draw_rectangle(colour, self.end_turn_location)

        text_surface = self.ui_text.render("End Turn", False, (0, 0, 0))
        center = (self.end_turn_location[0][0] + 5, self.end_turn_location[0][1] + 15)
        self.game_display.blit(text_surface, center)

    def check_where_mouse_clicked(self, pos):
        if (pos[0] >= self.end_turn_location[0][0] and pos[0] <= self.end_turn_location[1][0] and
            pos[1] >= self.end_turn_location[1][0] and pos[1] <= self.end_turn_location[1][1]):
            #mouse in end turn box
            self.ui_element_clicked[0] = True
            