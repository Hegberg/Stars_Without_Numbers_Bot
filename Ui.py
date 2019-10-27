
import pygame

import Draw
import Colour
import Goals
import Assets

class Ui:
    def __init__(self, draw, x, y):
        self.x = x
        self.y = y
        self.draw = draw
        #self.ui_text = pygame.font.Font('freesansbold.ttf',20)
        self.ui_text = pygame.font.SysFont("timesnewroman", 20)
        self.end_turn_dimensions = [(0,self.y - 50), (100, 50)]#top left point, dimensions
        self.actions_dimensions = [(150,self.y - 50), (100, 50)]#top left point, dimensions
        self.goals_dimensions = [(300,self.y - 50), (100, 50)]#top left point, dimensions

        self.return_to_systems_dimensions = [(0,self.y - 100), (100, 100)]#top left point, dimensions

        self.asset_selection_dimensions = [(500, 50), (250, 50)]#top left point, dimensions

        self.end_turn_rect = None
        self.actions_rect = None
        self.goals_rect = None

        self.faction_info_location = (450,self.y - 90)
        self.action_info_location = (0,0)

        self.amount_of_ui_elements = 3
        self.ui_element_clicked = [0] * self.amount_of_ui_elements
        self.ui_sub_element_clicked = [0] * 11 #largest amount of sub menu options
        self.ui_asset_element_clicked = [0] #need to expand each time used for size of menu

        self.sub_action_buttons = [None] * 9
        self.sub_goal_buttons = [None] * 11
        self.ui_asset_button = [None] #need to expand each time used for size of menu

        self.sub_action_button_texts = ["Attack", "Buy Asset", "Change Homeworld", "Expand Influence", "Refit Asset", 
                                        "Repair Asset/Faction", "Sell Asset", "Seize Planet", "Use Asset Ability"]

        self.sub_goal_button_texts = ["Blood The Enemy", "Commercial Expansion", "Destroy the Foe", "Expand Influence", 
                                        "Inside Enemy Territory", "Intelligence Coup", "Invincible Valor", "Military Conquest", 
                                        "Peaceable Kingdom", "Planetary Seizure", "Wealth of Worlds"]

        self.current_action = None
        self.current_goal = None
        self.selecting_asset = False

        self.cunning_assets = Assets.all_cunning_assets

    def draw_ui_buttons(self):
        #only draw end turn in system view, if in inner system have return to system
        if (self.ui_element_clicked[0] and self.draw.current_view == 0):
            self.draw_end_turn(Colour.gray)
        elif (self.draw.current_view == 0):
            self.draw_end_turn(Colour.white)
        elif (self.ui_element_clicked[0] and self.draw.current_view == 1):
            self.draw_return_to_systems(Colour.gray)
        elif (self.draw.current_view == 1):
            self.draw_return_to_systems(Colour.white)

        if (self.ui_element_clicked[1]):
            #grey button and create sub menu
            self.draw_actions(Colour.gray)
            self.draw_actions_sub_menu()
        else:
            self.draw_actions(Colour.white)

        if (self.ui_element_clicked[2]):
            self.draw_goals(Colour.gray)
            self.draw_goals_sub_menu()
        else:
            self.draw_goals(Colour.white)

    def clear_ui_elements(self):
        for i in range(0, self.amount_of_ui_elements):
            self.ui_element_clicked[i] = 0
        self.selecting_asset = False

    def draw_end_turn(self, colour):
        self.end_turn_rect = self.draw.draw_rectangle(colour, self.end_turn_dimensions)
        self.draw.draw_rectangle(Colour.dark_gray, self.end_turn_dimensions, 3)

        text_surface = self.ui_text.render("End Turn", False, (0, 0, 0))
        center = (self.end_turn_dimensions[0][0] + 5, self.end_turn_dimensions[0][1] + 15)
        self.draw.game_display.blit(text_surface, center)

    def draw_actions(self, colour):
        self.actions_rect = self.draw.draw_rectangle(colour, self.actions_dimensions)
        self.draw.draw_rectangle(Colour.dark_gray, self.actions_dimensions, 3)

        text_surface = self.ui_text.render("Actions", False, (0, 0, 0))
        center = (self.actions_dimensions[0][0] + 5, self.actions_dimensions[0][1] + 15)
        self.draw.game_display.blit(text_surface, center)

    def draw_goals(self, colour):
        self.goals_rect = self.draw.draw_rectangle(colour, self.goals_dimensions)
        self.draw.draw_rectangle(Colour.dark_gray, self.goals_dimensions, 3)

        text_surface = self.ui_text.render("Goals", False, (0, 0, 0))
        center = (self.goals_dimensions[0][0] + 5, self.goals_dimensions[0][1] + 15)
        self.draw.game_display.blit(text_surface, center)

    def draw_return_to_systems(self, colour):
        self.end_turn_rect = self.draw.draw_rectangle(colour, self.return_to_systems_dimensions)
        self.draw.draw_rectangle(Colour.dark_gray, self.return_to_systems_dimensions, 3)

        text_surface = self.ui_text.render("Return To", False, (0, 0, 0))
        center = (self.return_to_systems_dimensions[0][0] + 5, self.return_to_systems_dimensions[0][1] + 15)
        self.draw.game_display.blit(text_surface, center)

        text_surface = self.ui_text.render("System", False, (0, 0, 0))
        center = (self.end_turn_dimensions[0][0] + 5, self.end_turn_dimensions[0][1] + 15)
        self.draw.game_display.blit(text_surface, center)


    def check_where_mouse_clicked(self):
        if (self.ui_element_clicked[1]):
            for i in range(len(self.sub_action_buttons)):
                result = self.check_sub_ui_box(i, self.sub_action_buttons[i])
                if (result):
                    self.current_action = i
                    self.clear_ui_elements() #action ui element slected, drop menu
                    #if selected action that needs another menu
                    if (self.current_action == 1 or self.current_action == 4 or self.current_action == 5 or self.current_action == 6 or self.current_action == 8):
                        self.selecting_asset = True
                    return 1 #once done checking sub buttons, no need to check rest,
                    #keep from checking possible objects behind it
            return 0

        if (self.ui_element_clicked[2]):
            for i in range(len(self.sub_goal_buttons)):
                result = self.check_sub_ui_box(i, self.sub_goal_buttons[i])
                if (result):
                    self.current_goal = i
                    self.draw.universe.factions[self.draw.universe.turn].goal = i
                    self.clear_ui_elements() #sub ui element slected, drop menu
            #print(self.ui_sub_element_clicked)
                    return 1 #once done checking sub buttons, no need to check rest, 
                    #keep from checking possible objects behind it
            return 0

        #asset menu selection open
        if (self.selecting_asset):
            for i in range(len(self.ui_asset_button)):
                for j in range(len(self.ui_asset_button[i])):
                    result = self.check_asset_ui_box(i, j, self.ui_asset_button[i][j])
                    if (result):
                        self.clear_ui_elements() #sub ui element slected, drop menu
                        return 1
            return 0

        if (self.check_ui_box(0, self.end_turn_rect)):
            return 1
        if (self.check_ui_box(1, self.actions_rect)):
            return 1
        if (self.check_ui_box(2, self.goals_rect)):
            return 1

        return 0

        #print(self.ui_element_clicked)

    def check_ui_box(self, ui_element, rect):
        if (rect.collidepoint(self.draw.mouse_pos) and
            self.draw.mouse_down):
            #mouse in ui box and mouse is being clicked not released in box
            self.ui_element_clicked[ui_element] = True
            return 1
        else:
            self.ui_element_clicked[ui_element] = False
            return 0

    def check_sub_ui_box(self, ui_element, rect):
        if (rect.collidepoint(self.draw.mouse_pos) and
            self.draw.mouse_down):
            #mouse in ui box and mouse is being clicked not released in box
            self.ui_sub_element_clicked[ui_element] = True
            return True
        else:
            self.ui_sub_element_clicked[ui_element] = False
            return False

    def check_asset_ui_box(self, ui_asset_index, ui_asset, rect):
        if (rect.collidepoint(self.draw.mouse_pos) and
            self.draw.mouse_down):
            #mouse in ui box and mouse is being clicked not released in box
            self.ui_asset_element_clicked[ui_asset_index][ui_asset] = True
            return True
        else:
            self.ui_asset_element_clicked[ui_asset_index][ui_asset] = False
            return False

    def draw_actions_sub_menu(self):
        for i in range(len(self.sub_action_buttons)): #draw bottom up but want alphabetical from top down, so reverse a few array indexs
            sub_dimensions = [(150,self.y - (50 * (len(self.sub_action_buttons) - 1 - i + 2))), (200, 50)]
            """
            try:
                if (self.sub_action_buttons[i].collidepoint(self.draw.mouse_pos)):
                    self.sub_action_buttons[i] = self.draw.draw_rectangle(Colour.gray, sub_dimensions)
                else:
                    self.sub_action_buttons[i] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
            except: #ui sub buttons not created yet
                self.sub_action_buttons[i] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
            """
            self.sub_action_buttons[i] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
            self.draw.draw_rectangle(Colour.dark_gray, sub_dimensions, 2)

            text_surface = self.ui_text.render(self.sub_action_button_texts[i], False, (0, 0, 0))
            center = (sub_dimensions[0][0] + 5, sub_dimensions[0][1] + 15)
            self.draw.game_display.blit(text_surface, center)
        
        
    def draw_goals_sub_menu(self):
        for i in range(len(self.sub_goal_buttons)):
            sub_dimensions = [(300,self.y - (50 * (len(self.sub_goal_buttons) - 1 - i + 2))), (200, 50)]
            """
            try:
                if (self.sub_goal_buttons[i].collidepoint(self.draw.mouse_pos)):
                    self.sub_goal_buttons[i] = self.draw.draw_rectangle(Colour.gray, sub_dimensions)
                else:
                    self.sub_goal_buttons[i] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
            except: #ui sub buttons not created yet
                self.sub_goal_buttons[i] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
            """
            self.sub_goal_buttons[i] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
            self.draw.draw_rectangle(Colour.dark_gray, sub_dimensions, 2)

            text_surface = self.ui_text.render(self.sub_goal_button_texts[i], False, (0, 0, 0))
            center = (sub_dimensions[0][0] + 5, sub_dimensions[0][1] + 15)
            self.draw.game_display.blit(text_surface, center)

    def draw_stats(self, faction):
        #Name
        self.draw.render_text("Faction: ", faction.name, self.faction_info_location[0] + 5, self.faction_info_location[1] + 0)
        #Hp
        self.draw.render_text("Hp: ", faction.hp, self.faction_info_location[0] + 5, self.faction_info_location[1] + 20)
        #Max Hp
        self.draw.render_text("Max Hp: ", faction.max_hp, self.faction_info_location[0] + 5, self.faction_info_location[1] + 40)
        #Exp
        self.draw.render_text("Experince: ", faction.experience, self.faction_info_location[0] + 5, self.faction_info_location[1] + 60)

        #Tags
        self.draw.render_text("Tags: ", faction.tags, self.faction_info_location[0] + 175, self.faction_info_location[1] + 0)
        #Homeworld
        self.draw.render_text("Homeworld: ", faction.homeworld.location.get_coords(), self.faction_info_location[0] + 175, self.faction_info_location[1] + 20)

        #Force Rating
        self.draw.render_text("Force Rating: ", faction.force_rating, self.faction_info_location[0] + 175, self.faction_info_location[1] + 40)
        #Wealth Rating
        self.draw.render_text("Wealth Rating: ", faction.wealth_rating, self.faction_info_location[0] + 175, self.faction_info_location[1] + 60)
        #Cunning Rating
        self.draw.render_text("Cunning Rating: ", faction.cunning_rating, self.faction_info_location[0] + 365, self.faction_info_location[1] + 40)
        #Faction Credits
        self.draw.render_text("Faction Credits: ", faction.fac_creds, self.faction_info_location[0] + 365, self.faction_info_location[1] + 60)

        #Homeworld
        self.draw.render_text("Colour: ", faction.colour, self.faction_info_location[0] + 365, self.faction_info_location[1] + 20)

    def draw_action_selected(self):
        if (self.current_action != None):
            self.draw.render_text("Action: ", self.sub_action_button_texts[self.current_action], self.action_info_location[0] + 5, self.action_info_location[1] + 5)
        else:
            self.draw.render_text("Action: None", "", self.action_info_location[0] + 5, self.action_info_location[1] + 5)
        pass

    def draw_goal_selected(self): #and progress
        if (self.draw.universe.factions[self.draw.universe.turn].goal != None):
            self.draw.render_text("Goal: ", self.sub_goal_button_texts[self.draw.universe.factions[self.draw.universe.turn].goal], self.action_info_location[0] + 305, self.action_info_location[1] + 5)
        else:
            self.draw.render_text("Goal: None", "", self.action_info_location[0] + 305, self.action_info_location[1] + 5)
        """
        if (self.current_goal != None):
            self.draw.render_text("Goal: ", self.sub_goal_button_texts[self.current_goal], self.action_info_location[0] + 305, self.action_info_location[1] + 5)
        else:
            self.draw.render_text("Goal: None", "", self.action_info_location[0] + 305, self.action_info_location[1] + 5)
        pass
        """

    def draw_sub_asset_selection(self):
        if (self.selecting_asset):
            self.draw_assets_from_list(self.cunning_assets)
            #temp = [Assets.cunning1_assets, Assets.cunning2_assets, Assets.cunning3_assets]
            #self.draw_assets_from_list(temp)
        pass

    def draw_assets_from_list(self, asset_list):
        self.ui_asset_element_clicked = []
        self.ui_asset_button = []
        current_total_index = 0
        #list of list of assets
        for i in range(len(asset_list)):
            self.ui_asset_element_clicked.append([0] * len(asset_list[i]))
            self.ui_asset_button.append([None] * len(asset_list[i]))
            for j in range(len(asset_list[i])):
                #sub_dimensions = self.asset_selection_dimensions
                sub_dimensions = [(self.asset_selection_dimensions[0][0],self.asset_selection_dimensions[0][1] * (current_total_index)),
                                    (self.asset_selection_dimensions[1][0], self.asset_selection_dimensions[1][1])]
                """
                try:
                    if (self.ui_asset_button[i][j].collidepoint(self.draw.mouse_pos)):
                        self.ui_asset_button[i][j] = self.draw.draw_rectangle(Colour.gray, sub_dimensions)
                    else:
                        self.ui_asset_button[i][j] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
                except: #ui sub buttons not created yet
                    self.ui_asset_button[i][j] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
                """
                self.ui_asset_button[i][j] = self.draw.draw_rectangle(Colour.white, sub_dimensions)
                #self.ui_asset_button[i].append(self.draw.draw_rectangle(Colour.white, sub_dimensions))
                self.draw.draw_rectangle(Colour.dark_gray, sub_dimensions, 2)

                text_surface = self.ui_text.render(asset_list[i][j].name, False, (0, 0, 0))
                center = (sub_dimensions[0][0] + 5, sub_dimensions[0][1] + 15)
                self.draw.game_display.blit(text_surface, center)

                current_total_index += 1