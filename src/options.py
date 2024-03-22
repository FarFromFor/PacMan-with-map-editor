"""game options and settings"""

import pygame
from sounds import Sound
from config import *


class Options:
    """class game options and settings"""
    def __init__(self, screen, conditions):
        self.screen = screen
        self.conditions = conditions
        self.sound = Sound()

    def print_opt(self):
        """function for printing options screen"""
        run = True
        ret = False
        action = False
        while run:
            pygame.display.update()
            self.screen.fill(pygame.Color(BACKGROUND_COLOR))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1, button2, button3 = pygame.mouse.get_pressed()

            if not button1 and ret:
                Sound().play_action_effect(CLICK, Sound.volume)
                self.conditions[1] = Sound.volume
                return self.conditions

            self.__print_difficulty_panel(mouse_x, mouse_y)
            self.__print_volume_panel(mouse_x, mouse_y)
            self.__print_difficulty_number(self.conditions[0])
            self.__print_volume_number(Sound.volume*Sound.max_vol)
            self.__print_back_button(mouse_x, mouse_y)
            action, ret = self.check_action(button1, mouse_x, mouse_y, [action, ret])
            self.tmp(button2, button3)
        return None

    def tmp(self, b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False

    def check_action(self, button1, mouse_x, mouse_y, action_ret):
        """function for checking user interactions"""
        in_button_diff_pl = Object().in_button(mouse_x, mouse_y, Object.Options().diff_pl_coord())
        in_button_diff_mi = Object().in_button(mouse_x, mouse_y, Object.Options().diff_mi_coord())
        in_button_vol_pl = Object().in_button(mouse_x, mouse_y, Object.Options().vol_pl_coord())
        in_button_vol_mi = Object().in_button(mouse_x, mouse_y, Object.Options().vol_min_coord())
        if button1 and in_button_diff_pl and not action_ret[0]:
            action_ret[0] = True
            if self.conditions[0] < 3:
                self.conditions[0] += 1
                Sound().play_action_effect(CLICK, Sound.volume)
        if button1 and in_button_diff_mi and not action_ret[0]:
            action_ret[0] = True
            if self.conditions[0] > 1:
                self.conditions[0] -= 1
                Sound().play_action_effect(CLICK, Sound.volume)

        if button1 and in_button_vol_pl and not action_ret[0]:
            action_ret[0] = True
            if Sound.volume < Sound.sound_delta * 5:
                Sound.volume += Sound.sound_delta
                Sound.volume = round(Sound.volume, 1)
                pygame.mixer.music.set_volume(Sound.volume)
                Sound().play_action_effect(CLICK, Sound.volume)

        if button1 and in_button_vol_mi and not action_ret[0]:
            action_ret[0] = True
            if Sound.volume > 0:
                Sound.volume -= Sound.sound_delta
                Sound.volume = round(Sound.volume, 1)
                pygame.mixer.music.set_volume(Sound.volume)
                Sound().play_action_effect(CLICK, Sound.volume)

        if not button1:
            action_ret[0] = False
        if button1 and Object().in_button(mouse_x, mouse_y, Object.Options().back_coordinates()):
            action_ret[1] = True

        return action_ret

    def __print_back_button(self, mouse_x, mouse_y):
        """function for printing back button"""
        if Object().in_button(mouse_x, mouse_y, Object.Options().back_coordinates()):
            self.screen.blit(pygame.image.load(BACK_PINK), (Object.Options().back_l_c_coord()))
        else:
            self.screen.blit(pygame.image.load(BACK_WHITE), (Object.Options().back_l_c_coord()))

    def __print_volume_panel(self, mouse_x, mouse_y):
        """function for printing volume panel"""
        if Object().in_button(mouse_x, mouse_y, Object.Options().vol_pl_coord()):
            self.screen.blit(pygame.image.load(VOLUME_P_W), (Object.Options().vol_coord()))
        elif Object().in_button(mouse_x, mouse_y, Object.Options().vol_min_coord()):
            self.screen.blit(pygame.image.load(VOLUME_W_P), (Object.Options().vol_coord()))
        else:
            self.screen.blit(pygame.image.load(VOLUME_V_V), (Object.Options().vol_coord()))

    def __print_difficulty_panel(self, mouse_x, mouse_y):
        """function for printing difficulty panel"""
        if Object().in_button(mouse_x, mouse_y, Object.Options().diff_pl_coord()):
            self.screen.blit(pygame.image.load(DIFFICULTY_P_W), (Object.Options().diff_coord()))
        elif Object().in_button(mouse_x, mouse_y, Object.Options().diff_mi_coord()):
            self.screen.blit(pygame.image.load(DIFFICULTY_W_P), (Object.Options().diff_coord()))
        else:
            self.screen.blit(pygame.image.load(DIFFICULTY_W_W), (Object.Options().diff_coord()))

    def __print_difficulty_number(self, number):
        """function for printing difficulty number"""
        if number == 1:
            self.screen.blit(pygame.image.load(ONE_ART), Object.Options().diff_num_coord())
        elif number == 2:
            self.screen.blit(pygame.image.load(TWO_ART), Object.Options().diff_num_coord())
        elif number == 3:
            self.screen.blit(pygame.image.load(THREE_ART), Object.Options().diff_num_coord())

    def __print_volume_number(self, number):
        """function for printing volume number"""
        if number == 0:
            self.screen.blit(pygame.image.load(ZERO_ART), Object.Options().vol_number_coord())
        elif number == 1:
            self.screen.blit(pygame.image.load(ONE_ART), Object.Options().vol_number_coord())
        elif number == 2:
            self.screen.blit(pygame.image.load(TWO_ART), Object.Options().vol_number_coord())
        elif number == 3:
            self.screen.blit(pygame.image.load(THREE_ART), Object.Options().vol_number_coord())
        elif number == 4:
            self.screen.blit(pygame.image.load(FOUR_ART), Object.Options().vol_number_coord())
        elif number == 5:
            self.screen.blit(pygame.image.load(FIVE_ART), Object.Options().vol_number_coord())
