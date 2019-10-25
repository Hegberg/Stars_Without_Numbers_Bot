import pygame
import math

import Colour
import Faction
import Universe
import Tile

import Ui

class Pygame_Object(object):
    
    def __init__(self, x, y, universe):
        self.game_display = None
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()

        self.pygame_init()
        #print(pygame.font.get_fonts())

        self.ui = Ui.Ui(self,x,y)

        self.mouse_down = False;
        self.mouse_released = True;

        self.mouse_pos = None

        self.universe = universe
        self.selected_system = None

        self.layout_rim = Tile.Layout(Tile.layout_pointy, Tile.Point(24,24), Tile.Point(x/2,y/2))
        self.layout = Tile.Layout(Tile.layout_pointy, Tile.Point(28,28), Tile.Point(x/2,y/2))

        self.current_view = 0 #0 -> universe view, 1 inner system view

        self.drawn_systems = [] #[hex, system] list items
        self.drawn_planets = []

        self.ui_text = pygame.font.SysFont("timesnewroman", 20)

    def pygame_init(self):
        pygame.init()

        self.game_display = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Faction Visualizer")

        pass


    def capture_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return -1

            self.mouse_pos = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                if (not(self.mouse_released)):
                    return 0
                if (self.ui.check_where_mouse_clicked()): 
                    return 0

                #if ui element not pressed, check if no ui sub menu open, if one is clear sub menu and return
                for i in range(len(self.ui.ui_element_clicked)):
                    if (self.ui.ui_element_clicked[i]):
                        self.ui.clear_ui_elements()
                        return 0
                #otherwise continue


                #self.check_where_mouse_clicked()
                if (self.check_where_mouse_clicked()):
                    return 0

                #if made here no ui element was clicked
                self.clear_ui_elements()
                #set mouse released to false, so other ui elemnts not interacted with until mouse up
                self.mouse_released = False
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
                self.mouse_released = True
                """
                if (self.ui.check_where_mouse_clicked()):
                    return 0
                self.check_where_mouse_clicked()
                """
                #print(self.ui_sub_element_clicked)
            #print(event)
        return 0

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def clear_ui_elements(self):
        self.ui.clear_ui_elements()

    def draw_polygon(self, colour, points):
        return pygame.draw.polygon(self.game_display, colour, points)

    def draw_rectangle(self, colour, points, width = 0):
        return pygame.draw.rect(self.game_display, colour, points, width)

    def draw_circle(self, colour, center, radius, width = 0):
        return pygame.draw.circle(self.game_display, colour, center, radius, width)

    def render_text(self, text, stat, x, y):
        text_surface = self.ui_text.render(text + str(stat), False, (255, 255, 255))
        center = (x, y)
        self.game_display.blit(text_surface, center)

    def check_where_mouse_clicked(self):
        #check current_view if in universe view
        if (self.current_view == 0 and self.mouse_down):
            for i in range(len(self.drawn_systems)):
                result = self.check_polygon(self.drawn_systems[i][0])
                if (result):
                    #change view to inner system view for the selected system
                    self.selected_system = self.drawn_systems[i][1]
                    self.current_view = 1
                    return 1

            return 0 #once done checking sub buttons, no need to check rest, 
                    #keep from checking possible objects behind it

        if (self.current_view == 1 and self.mouse_down):

            return 0 #once done checking sub buttons, no need to check rest, 
                    #keep from checking possible objects behind it
        #except: #sub ui wasn't created yet
            #print(e)
            #pass

    #get math to check if in polygon
    def check_polygon(self, polygon):
        #check if in sphere matching rouchly hex size
        #print(polygon)
        radius = math.sqrt(math.pow(polygon[0][0] - polygon[3][0], 2) + math.pow(polygon[0][1] - polygon[3][1], 2)) /2 
        #radius has / 2 because rest of equation is jjust distance between points
        x_avg = ((polygon[0][0] + polygon[3][0]) / 2)
        y_avg = ((polygon[0][1] + polygon[3][1]) / 2)
        """
        if(math.pow(self.mouse_pos[0] - (x_avg, 2) + math.pow(self.mouse_pos[1] - (y_avg, 2) < math.pow(radius,2)):

            #show where the circle was clicked is
            pygame.draw.circle(self.game_display, Colour.gray, (int(x_avg), int(y_avg)), int(radius))
            """
        return (math.pow(self.mouse_pos[0] - x_avg, 2) + math.pow(self.mouse_pos[1] - y_avg, 2) < math.pow(radius,2))

    def turn_end(self):
        self.ui.current_action = None
        self.ui.current_goal = None

    def turn_start(self):
        self.ui.current_action = None
        self.ui.current_goal = self.universe.factions[self.universe.turn].goal

    def hex_point_to_pygame_point(self, points):#list of hex points
        pygame_points = []
        for point in points:
            pygame_points.append((point.x, point.y))

        return pygame_points

    def draw_universe_view(self):
        self.drawn_systems.clear()
        for system in self.universe.universe_map:
            #white tiling behind systems
            points = Tile.polygon_corners(self.layout, self.universe.universe_map[system].location)
            new_points = self.hex_point_to_pygame_point(points)

            self.draw_polygon(Colour.white, new_points)

        for system in self.universe.universe_map:
            #systems with spacing in between
            points = Tile.polygon_corners_with_spacing(self.layout_rim, self.universe.universe_map[system].location, 1.155)
            new_points = self.hex_point_to_pygame_point(points)

            if (self.universe.universe_map[system].controlling_faction != None):
                self.drawn_systems.append([new_points, self.universe.universe_map[system]])
                self.draw_polygon(self.universe.universe_map[system].controlling_faction.colour, new_points)
                #print(universe.universe_map[system].faction.colour)
            else:
                self.drawn_systems.append([new_points, self.universe.universe_map[system]])
                self.draw_polygon(Colour.black, new_points)

    def draw_inner_system_view(self):
        self.drawn_planets.clear()

        x_start = (self.x/2) - ((len(self.selected_system.planets) - 1) * 100)

        for i in range(len(self.selected_system.planets)):
            self.draw_circle(self.selected_system.planets[i].planet_type.colour, (int(x_start + (i * 200)), int(self.y/2)), 50) #colour, center, radius


    def draw_view(self):
        if (self.current_view == 0):#universe view
            self.draw_universe_view()
        elif (self.current_view == 1):
            self.draw_inner_system_view()

    def draw_ui(self, faction):
        self.ui.draw_stats(faction)
        self.ui.draw_action_selected()
        self.ui.draw_goal_selected()

        self.ui.draw_ui_buttons()