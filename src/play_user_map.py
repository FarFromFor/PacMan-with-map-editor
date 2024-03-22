"""play user maps"""

import time
import copy
import pygame
from sounds import Sound
from play import Play
from config import *


class PlayUserMap:
    """class for playing user maps"""
    def __init__(self, screen, status):
        self.sc = screen
        self.count = 0
        self.maps = len(status.user_maps)
        self.sw = [False, False]
        self.status_def = status
        self.user_maps = copy.deepcopy(status.user_maps)
        self.delete = False

    def choose_map_panel(self):
        """function for choosing user maps"""
        run = True
        ret = False
        button1, button2, button3 = pygame.mouse.get_pressed()
        if button1:
            time.sleep(0.08)
        while run:
            time.sleep(FPS_LOCK)
            pygame.display.update()
            self.sc.fill(pygame.Color(BACKGROUND_COLOR))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False, ''

            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1, button2, button3 = pygame.mouse.get_pressed()
            if ret and not button1:
                Sound().play_action_effect(CLICK, Sound.volume)
                return False, ''
            self.__check_switch(button1)
            self.__print_back_button(mouse_x, mouse_y)
            self.__print_play_button(mouse_x, mouse_y)
            self.__print_delete_button(mouse_x, mouse_y)
            self.__print_switch_left_button(mouse_x, mouse_y)
            self.__print_switch_right_button(mouse_x, mouse_y)
            self.__print_text_input(self.count)
            ret, play = self.__check_action(button1, mouse_x, mouse_y)
            if play and self.maps != 0:
                Sound().play_background_music(USER_MAP_MUSIC, Sound.volume)
                pygame.mixer.music.set_volume(Sound.volume)
                Play(self.sc, self.status_def, self.user_maps[self.count][1]).play_map(self.sc)
                Sound().play_background_music(MENU_MUSIC, Sound.volume)
                pygame.mixer.music.set_volume(Sound.volume)
            if self.delete and not button1:
                Sound().play_action_effect(CLICK, Sound.volume)
                self.__delete_map()
                self.delete = False
            self.dum_f(button2, button3)
        return False, ''

    def dum_f(self, b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False

    def __delete_map(self):
        """function for deleting user maps"""
        if len(self.user_maps) == 0:
            return
        del self.user_maps[self.count]
        self.count = 0
        self.maps -= 1
        self.status_def.user_maps = self.user_maps

    def __print_text_input(self, map_counter):
        """function for printing text input"""
        self.sc.blit(pygame.image.load(RACT_ART), (INPUT_TXT_BAR_X, INPUT_TXT_BAR_Y))
        pygame.display.set_caption('')
        font = pygame.font.Font(None, INPUT_TXT_SIZE)
        if self.maps != 0:
            text_surface = font.render(self.user_maps[map_counter][0], True, INPUT_TXT_COLOR)
            self.sc.blit(text_surface, (INPUT_TXT_X, INPUT_TXT_Y))

    def __check_switch(self, button1):
        """function for playing user maps"""
        if self.maps == 0:
            return
        if not button1 and self.sw[0]:
            if self.count < self.maps - 1:
                self.count += 1
            else:
                self.count = 0
            Sound().play_action_effect(CLICK, Sound.volume)
            self.sw[0] = False
        if not button1 and self.sw[1]:
            if self.count > 0:
                self.count -= 1
            else:
                self.count = self.maps - 1
            Sound().play_action_effect(CLICK, Sound.volume)
            self.sw[1] = False

    def __check_action(self, button1, mouse_x, mouse_y):
        """function for checking user interactions"""
        if button1 and Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().back_coord()):
            return True, False
        if button1 and Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().play_coord()):
            if self.maps == 0:
                return False, False
            return True, True
        if button1 and Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().sw_r_coord()):
            self.sw[0] = True
        if button1 and Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().sw_l_coord()):
            self.sw[1] = True
        if button1 and Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().del_coord()):
            self.delete = True
        return False, False

    def __print_switch_left_button(self, mouse_x, mouse_y):
        """function for printing left switch button"""
        if Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().sw_l_coord()):
            self.sc.blit(pygame.image.load(SWITCH_LEFT_PINK),
                         (Object.PlayUserMapScr().sw_l_l_cor_coord()))
        else:
            self.sc.blit(pygame.image.load(SWITCH_LEFT_WHITE),
                         (Object.PlayUserMapScr().sw_l_l_cor_coord()))

    def __print_switch_right_button(self, mouse_x, mouse_y):
        """function for printing right switch button"""
        if Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().sw_r_coord()):
            self.sc.blit(pygame.image.load(SWITCH_RIGHT_PINK),
                         (Object.PlayUserMapScr().switch_right_left_corner_coordinates()))
        else:
            self.sc.blit(pygame.image.load(SWITCH_RIGHT_WHITE),
                         (Object.PlayUserMapScr().switch_right_left_corner_coordinates()))

    def __print_delete_button(self, mouse_x, mouse_y):
        """function for printing delete button"""
        if Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().del_coord()):
            self.sc.blit(pygame.image.load(DELETE_RED),
                         (Object.PlayUserMapScr().delete_left_corner_coordinates()))
        else:
            self.sc.blit(pygame.image.load(DELETE_WHITE),
                         (Object.PlayUserMapScr().delete_left_corner_coordinates()))

    def __print_back_button(self, mouse_x, mouse_y):
        """function for printing back button"""
        if Object().in_button(mouse_x, mouse_y, Object.PlayUserMapScr().back_coord()):
            self.sc.blit(pygame.image.load(BACK_PINK),
                         (Object.PlayUserMapScr().back_left_corner_coordinates()))
        else:
            self.sc.blit(pygame.image.load(BACK_WHITE),
                         (Object.PlayUserMapScr().back_left_corner_coordinates()))

    def __print_play_button(self, mouse_x, mouse_y):
        """function for printing play button"""
        if Object().in_button(mouse_x, mouse_y, Object.SaveNameScr().save_coord()):
            self.sc.blit(pygame.image.load(PLAY_SMALL_PINK),
                         (Object.SaveNameScr().save_l_c_coord()))
        else:
            self.sc.blit(pygame.image.load(PLAY_SMALL_WHITE),
                         (Object.SaveNameScr().save_l_c_coord()))
