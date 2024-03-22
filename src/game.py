"""game menu and options"""

import random
import time
import pygame
from creator import Creator
from options import Options
from sounds import Sound
from upload import Upload
from play_user_map import PlayUserMap
from play import Play
from game_status import Status
from config import *


class Char:
    """class for creating game characters: pacman and ghosts"""
    def __init__(self, itself):
        self.way = round(random.uniform(WAY_L_R, WAY_R_L))
        self.char_x = LEFT_BORDER
        self.char_y = random.uniform(BOTTOM_SCREEN, TOP_SCREEN)
        self.itself = itself
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        if self.way == WAY_L_R:
            self.char_x = LEFT_BORDER
            self.char_y = random.uniform(BOTTOM_SCREEN, TOP_SCREEN)
            self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        else:
            self.char_x = RIGHT_BORDER
            self.char_y = random.uniform(BOTTOM_SCREEN, TOP_SCREEN)
            self.speed = random.uniform(- MIN_SPEED, - MAX_SPEED)

    def print_char(self, screen):
        """printing character"""
        screen.blit(pygame.image.load(self.itself), (self.char_x, self.char_y))
        self.char_x += self.speed
        if self.char_x > RIGHT_BORDER or self.char_x < LEFT_BORDER:
            if self.way == WAY_L_R:
                self.char_x = LEFT_BORDER
                self.char_y = random.uniform(BOTTOM_SCREEN, TOP_SCREEN)
                self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
            else:
                self.char_x = RIGHT_BORDER
                self.char_y = random.uniform(BOTTOM_SCREEN, TOP_SCREEN)
                self.speed = random.uniform(- MIN_SPEED, - MAX_SPEED)
            self.way = round(random.uniform(WAY_L_R, WAY_R_L))

    def tmp(self, b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False


class Game:
    """class for main game"""
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.status = Status()
        self.ghost_red = Char(GHOST_RED_ART)
        self.ghost_blue = Char(GHOST_BLUE_ART)
        self.ghost_yellow = Char(GHOST_YELLOW_ART)
        self.ghost_green = Char(GHOST_GREEN_ART)

    def start_game(self):
        """function for starting the game"""
        self.status = Upload().upload_all()
        self.__start()
        ghost_down1 = Char(GHOST_DOWN_ART)
        ghost_down2 = Char(GHOST_DOWN_ART)
        ghost_down3 = Char(GHOST_DOWN_ART)
        run = True
        self.status.current_map = 0
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            time.sleep(FPS_LOCK)
            pygame.display.update()
            self.screen.fill(pygame.Color(BACKGROUND_COLOR))
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1, button2, button3 = pygame.mouse.get_pressed()
            self.__print_version()
            self.__move_ghosts()
            self.__move_ghosts_down(ghost_down1, ghost_down2, ghost_down3)
            self.__print_button(mouse_x, mouse_y)

            # PLAY
            if button1 and self.in_button_number(mouse_x, mouse_y) == PLAY:
                Sound().play_action_effect(CLICK, Sound.volume)
                play_game = True
                while play_game:
                    self.__play_sound(self.status.current_map)

                    map_tmp = self.status.history_maps[self.status.current_map][1]
                    if Play(self.screen, self.status, map_tmp).play_map(self.screen):
                        self.status.current_map += 1
                        self.status.current_map %= COMPANY_MAPS_AMOUNT
                    else:
                        play_game = False
                self.__return_menu_music()

            # CREATE LEVEL
            elif button1 and self.in_button_number(mouse_x, mouse_y) == CREATE_LEVEL:
                Sound().play_action_effect(CLICK, Sound.volume)
                run, game_map = Creator(self.screen, self.status.conditions).create_map()
                if len(game_map) == 2:
                    self.status.user_maps.append(game_map)
                Upload().save_all(self.status)

            # PLAY USER MAP
            elif button1 and self.in_button_number(mouse_x, mouse_y) == PLAY_USER_MAP:
                Sound().play_action_effect(CLICK, Sound.volume)
                PlayUserMap(self.screen, self.status).choose_map_panel()

            # OPTIONS
            elif button1 and self.in_button_number(mouse_x, mouse_y) == OPTIONS:
                Sound().play_action_effect(CLICK, Sound.volume)
                self.status.conditions = Options(self.screen, self.status.conditions).print_opt()
                pygame.mixer.music.set_volume(Sound.volume)
                Upload().save_all(self.status)

            # EXIT
            elif button1 and self.in_button_number(mouse_x, mouse_y) == EXIT:
                Sound().play_action_effect(CLICK, Sound.volume)
                Upload().save_all(self.status)
                time.sleep(0.2)
                pygame.quit()
                return
            self.tmp(button2, button3)

    def __return_menu_music(self):
        """returns memu music after changing"""
        Sound().play_background_music(MENU_MUSIC, Sound.volume)
        pygame.mixer.music.set_volume(Sound.volume)
        pygame.mixer.music.play(-1)

    def __start(self):
        """starts playing music in the game"""
        pygame.init()
        pygame.display.set_caption(NAME_OF_GAME)
        Sound.volume = self.status.conditions[1]
        Sound().play_background_music(MENU_MUSIC, Sound.volume)
        pygame.mixer.music.set_volume(Sound.volume)
        pygame.mixer.music.play(-1)

    def __play_sound(self, music_num):
        """plays music for specific level"""
        if music_num == 0:
            Sound().play_background_music(LEVEL_0_MUSIC, Sound.volume)
        elif music_num == 1:
            Sound().play_background_music(LEVEL_1_MUSIC, Sound.volume)
        elif music_num == 2:
            Sound().play_background_music(LEVEL_2_MUSIC, Sound.volume)
        elif music_num == 3:
            Sound().play_background_music(LEVEL_3_MUSIC, Sound.volume)
        pygame.mixer.music.set_volume(Sound.volume)
        pygame.mixer.music.play(-1)

    def tmp(self, b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False

    def __move_ghosts_down(self, g1, g2, g3):
        """downed ghosts making a step"""
        g1.print_char(self.screen)
        g2.print_char(self.screen)
        g3.print_char(self.screen)

    def __move_ghosts(self):
        """ghosts making a step"""
        self.ghost_red.print_char(self.screen)
        self.ghost_blue.print_char(self.screen)
        self.ghost_green.print_char(self.screen)
        self.ghost_yellow.print_char(self.screen)

    def __print_version(self):
        """print current game version"""
        font = pygame.font.Font(None, VERSION_DONT_SIZE)
        text_surface = font.render(SIGN, True, VERSION_COLOR)
        self.screen.blit(text_surface, (VERSION_X, VERSION_Y))

    def in_button_number(self, x, y):
        """function for checking user interactions with buttons"""
        if Object().in_button(x, y, Object.Menu().button1_coordinates()):
            return 1
        if Object().in_button(x, y, Object.Menu().button2_coordinates()):
            return 2
        if Object().in_button(x, y, Object.Menu().button3_coordinates()):
            return 3
        if Object().in_button(x, y, Object.Menu().button4_coordinates()):
            return 4
        if Object().in_button(x, y, Object.Menu().button5_coordinates()):
            return 5
        return None

    def __print_button(self, mouse_x, mouse_y):
        """function for printing buttons"""
        b1c = Object.Menu().button1_l_c_coord()
        b2c = Object.Menu().button2_l_c_coord()
        b3c = Object.Menu().button3_l_c_coord()
        b4c = Object.Menu().button4_l_c_coord()
        b5c = Object.Menu().button5_l_c_coord()
        self.screen.blit(pygame.image.load(PLAY_BLACK), b1c)
        self.screen.blit(pygame.image.load(CREATE_LVL_BLACK), b2c)
        self.screen.blit(pygame.image.load(PLAY_USER_MAP_BLACK), b3c)
        self.screen.blit(pygame.image.load(OPTIONS_BLACK), b4c)
        self.screen.blit(pygame.image.load(EXIT_BLACK), b5c)

        buttons = {
            1: lambda: self.screen.blit(pygame.image.load(PLAY_WHITE), b1c),
            2: lambda: self.screen.blit(pygame.image.load(CREATE_LVL_WHITE), b2c),
            3: lambda: self.screen.blit(pygame.image.load(PLAY_USER_MAP_WHITE), b3c),
            4: lambda: self.screen.blit(pygame.image.load(OPTIONS_WHITE), b4c),
            5: lambda: self.screen.blit(pygame.image.load(EXIT_WHITE), b5c)
        }

        buttons.get(self.in_button_number(mouse_x, mouse_y), lambda: None)()
