import pygame

import Colour
import Faction

class Pygame_Object(object):
    
    def __init__(self, x, y):
        self.game_display = None
        self.x = x
        self.y = y
        self.clock = pygame.time.Clock()

        self.pygame_init()
        #print(pygame.font.get_fonts())
        #self.ui_text = pygame.font.Font('freesansbold.ttf',20)
        self.ui_text = pygame.font.SysFont("timesnewroman", 20)
        self.end_turn_dimensions = [(0,self.y - 50), (100, 50)]#top left point, dimensions
        self.actions_dimensions = [(150,self.y - 50), (100, 50)]#top left point, dimensions
        self.goals_dimensions = [(300,self.y - 50), (100, 50)]#top left point, dimensions

        self.end_turn_rect = None
        self.actions_rect = None
        self.goals_rect = None

        self.faction_info_location = (450,self.y - 90)

        self.mouse_down = False;
        self.mouse_released = False;

        self.amount_of_ui_elements = 3
        self.ui_element_clicked = [0] * self.amount_of_ui_elements

        self.sub_action_buttons = [None] * 9
        self.sub_goal_buttons = [None] * 1

        self.sub_action_button_texts = ["Attack", "Buy Asset", "Change Homeworld", "Expand Influence", "Refit Asset", 
                                        "Repair Asset/Faction", "Sell Asset", "Seize Planet", "Use Asset Ability"]

        self.sub_goal_button_texts = ["Attack", "Buy Asset", "Change Homeworld", "Expand Influence", "Refit Asset", 
                                        "Repair Asset/Faction", "Sell Asset", "Seize Planet", "Use Asset Ability"]

        self.mouse_pos = None

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
                self.check_where_mouse_clicked()
            if event.type == pygame.MOUSEBUTTONUP:
                self.check_where_mouse_clicked()
                self.mouse_down = False
                self.mouse_released = True
            #print(event)
        return 0

    def update(self):
        pygame.display.update()
        self.clock.tick(60)

    def clear_ui_elements(self):
        for i in range(0, self.amount_of_ui_elements):
            self.ui_element_clicked[i] = 0

    def draw_polygon(self, colour, points):
        return pygame.draw.polygon(self.game_display, colour, points)

    def draw_rectangle(self, colour, points, width = 0):
        return pygame.draw.rect(self.game_display, colour, points, width)

    def draw_ui_buttons(self):
        if (self.ui_element_clicked[0]):
            self.draw_end_turn(Colour.gray)
        else:
            self.draw_end_turn(Colour.white)

        if (self.ui_element_clicked[1]):
            #grey button and create sub menu
            self.draw_actions(Colour.gray)
            self.draw_actions_sub_menu()
        else:
            self.draw_actions(Colour.white)

        if (self.ui_element_clicked[2]):
            self.draw_goals(Colour.gray)
        else:
            self.draw_goals(Colour.white)

    def draw_end_turn(self, colour):
        self.end_turn_rect = self.draw_rectangle(colour, self.end_turn_dimensions)
        self.draw_rectangle(Colour.dark_gray, self.end_turn_dimensions, 3)

        text_surface = self.ui_text.render("End Turn", False, (0, 0, 0))
        center = (self.end_turn_dimensions[0][0] + 5, self.end_turn_dimensions[0][1] + 15)
        self.game_display.blit(text_surface, center)

    def draw_actions(self, colour):
        self.actions_rect = self.draw_rectangle(colour, self.actions_dimensions)
        self.draw_rectangle(Colour.dark_gray, self.actions_dimensions, 3)

        text_surface = self.ui_text.render("Actions", False, (0, 0, 0))
        center = (self.actions_dimensions[0][0] + 5, self.actions_dimensions[0][1] + 15)
        self.game_display.blit(text_surface, center)

    def draw_goals(self, colour):
        self.goals_rect = self.draw_rectangle(colour, self.goals_dimensions)
        self.draw_rectangle(Colour.dark_gray, self.goals_dimensions, 3)

        text_surface = self.ui_text.render("Goals", False, (0, 0, 0))
        center = (self.goals_dimensions[0][0] + 5, self.goals_dimensions[0][1] + 15)
        self.game_display.blit(text_surface, center)

    def check_where_mouse_clicked(self):
        self.check_ui_box(0, self.end_turn_rect)
        self.check_ui_box(1, self.actions_rect)
        self.check_ui_box(2, self.goals_rect)

    def check_ui_box(self, ui_element, rect):
        if (rect.collidepoint(self.mouse_pos) and
            self.mouse_down):
            #mouse in ui box and mouse is being clicked not released in box
            self.ui_element_clicked[ui_element] = True
        else:
            self.ui_element_clicked[ui_element] = False

    def draw_actions_sub_menu(self):
        for i in range(len(self.sub_action_buttons)):
            sub_dimensions = [(150,self.y - (50 * (i + 2))), (200, 50)]
            try:
                if (self.sub_action_buttons[i].collidepoint(self.mouse_pos)):
                    self.sub_action_buttons[i] = self.draw_rectangle(Colour.gray, sub_dimensions)
                else:
                    self.sub_action_buttons[i] = self.draw_rectangle(Colour.white, sub_dimensions)
            except: #ui sub buttons not created yet
                self.sub_action_buttons[i] = self.draw_rectangle(Colour.white, sub_dimensions)
            self.draw_rectangle(Colour.dark_gray, sub_dimensions, 2)

            text_surface = self.ui_text.render(self.sub_action_button_texts[i], False, (0, 0, 0))
            center = (sub_dimensions[0][0] + 5, sub_dimensions[0][1] + 15)
            self.game_display.blit(text_surface, center)
        
        
    def draw_goals_sub_menu(self):
        pass

    def draw_stats(self, faction):
        #Name
        self.render_text("Faction: ", faction.name, self.faction_info_location[0] + 5, self.faction_info_location[1] + 0)
        #Hp
        self.render_text("Hp: ", faction.hp, self.faction_info_location[0] + 5, self.faction_info_location[1] + 20)
        #Max Hp
        self.render_text("Max Hp: ", faction.max_hp, self.faction_info_location[0] + 5, self.faction_info_location[1] + 40)
        #Exp
        self.render_text("Experince: ", faction.experience, self.faction_info_location[0] + 5, self.faction_info_location[1] + 60)

        #Tags
        self.render_text("Tags: ", faction.tags, self.faction_info_location[0] + 175, self.faction_info_location[1] + 0)
        #Homeworld
        self.render_text("Homeworld: ", faction.homeworld, self.faction_info_location[0] + 175, self.faction_info_location[1] + 20)

        #Force Rating
        self.render_text("Force Rating: ", faction.force_rating, self.faction_info_location[0] + 175, self.faction_info_location[1] + 40)
        #Wealth Rating
        self.render_text("Wealth Rating: ", faction.wealth_rating, self.faction_info_location[0] + 175, self.faction_info_location[1] + 60)
        #Cunning Rating
        self.render_text("Cunning Rating: ", faction.cunning_rating, self.faction_info_location[0] + 345, self.faction_info_location[1] + 40)
        #Faction Credits
        self.render_text("Faction Credits: ", faction.fac_creds, self.faction_info_location[0] + 345, self.faction_info_location[1] + 60)

    def render_text(self, text, stat, x, y):
        text_surface = self.ui_text.render(text + str(stat), False, (255, 255, 255))
        center = (x, y)
        self.game_display.blit(text_surface, center)