
from Draw import Pygame_Object
import pygame, random

import Colour
import SaveLoad

import Universe
import Tile
import Planet
import Faction

def hex_point_to_pygame_point(points):#list of hex points
    pygame_points = []
    for point in points:
        pygame_points.append((point.x, point.y))

    return pygame_points


def main():
    x = 1000
    y = 800

    try:
        universe = SaveLoad.load_universe("universe")
    except:
        map_size = 5
        universe = Universe.Universe()
        #currently need more things before going over faction size 8
        universe.create_map(map_size)
        universe.create_factions(map_size + 3)

    #pygame_object = Pygame_Object(1920,1080)
    pygame_object = Pygame_Object(x,y)

    error = 0

    layout = Tile.Layout(Tile.layout_pointy, Tile.Point(24,24), Tile.Point(x/2,y/2))
    layout_rim = Tile.Layout(Tile.layout_pointy, Tile.Point(28,28), Tile.Point(x/2,y/2))

    while (error == 0):

        pygame_object.game_display.fill(Colour.black)

        error = pygame_object.capture_events()
        #Ui elements selected here
        if (pygame_object.mouse_released):
            #mouse button finished clicking button
            if (pygame_object.ui_element_clicked[0]): #end turn button clicked
                universe.turn = (universe.turn + 1) % len(universe.factions)
                pygame_object.turn_end()


            pygame_object.mouse_released = False
            pygame_object.clear_ui_elements()

        for planet in universe.universe_map:

            points = Tile.polygon_corners(layout_rim, universe.universe_map[planet].location)
            new_points = hex_point_to_pygame_point(points)

            pygame_object.draw_polygon(Colour.white, new_points)

        for planet in universe.universe_map:
            #white tiling behind systems
            points = Tile.polygon_corners_with_spacing(layout, universe.universe_map[planet].location, 1.155)
            new_points = hex_point_to_pygame_point(points)

            if (universe.universe_map[planet].faction != None):
                pygame_object.draw_polygon(universe.universe_map[planet].faction.colour, new_points)
                #print(universe.universe_map[planet].faction.colour)
            else:
                pygame_object.draw_polygon(Colour.black, new_points)

        pygame_object.draw_stats(universe.factions[universe.turn])
        pygame_object.draw_action_selected()
        pygame_object.draw_goal_selected()

        pygame_object.draw_ui_buttons()
    
        pygame_object.update()

    SaveLoad.save_universe("universe", universe)

if __name__ == '__main__':
    main()