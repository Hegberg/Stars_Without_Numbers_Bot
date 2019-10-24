
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
    pygame_object = Pygame_Object(x,y, universe)

    error = 0

    while (error == 0):

        pygame_object.game_display.fill(Colour.black)

        pygame_object.draw_view()

        pygame_object.draw_ui(universe.factions[universe.turn])

        #draw everything, then capture events

        error = pygame_object.capture_events()
        #Ui elements selected here
        if (pygame_object.mouse_down):
            #mouse button finished clicking button
            if (pygame_object.ui.ui_element_clicked[0] and pygame_object.current_view == 0): #end turn button clicked
                universe.turn = (universe.turn + 1) % len(universe.factions)
                pygame_object.turn_end()
                pygame_object.clear_ui_elements()

            elif (pygame_object.ui.ui_element_clicked[0] and pygame_object.current_view == 1):
                pygame_object.current_view = 0
                pygame_object.clear_ui_elements()


            #pygame_object.mouse_released = False
            # pygame_object.clear_ui_elements()
    
        pygame_object.update()

    SaveLoad.save_universe("universe", universe)

if __name__ == '__main__':
    main()