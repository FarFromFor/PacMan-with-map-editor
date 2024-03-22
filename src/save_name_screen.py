"""save screen class and functions"""
import time
import pygame
from sounds import Sound
from config import *


class SaveScreen:
    """class for creating a save screen"""
    def __init__(self, screen, conditions):
        self.screen = screen
        self.conditions = conditions

    def save(self):
        """function for creating a save screen"""
        run = True
        ret = False
        save = False
        input_text = ''
        while run:
            pygame.display.update()
            time.sleep(FPS_LOCK)
            self.screen.fill(pygame.Color(BACKGROUND_COLOR))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False, ''
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                        continue
                    if len(input_text) <= MAX_TXT_INPUT_LEN:
                        tmp = ''
                        tmp += event.unicode
                        if tmp.isascii():
                            input_text += tmp

            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1, button2, button3 = pygame.mouse.get_pressed()
            self.tmp(button2, button3)
            if ret and not button1:
                Sound().play_action_effect(CLICK, Sound.volume)
                if save:
                    Sound().play_action_effect(TOASTY, Sound.volume)
                    time.sleep(SLEEP_AFTER_SAVE)
                    return True, input_text
                return False, ''

            self.__print_back_button(mouse_x, mouse_y)
            self.__print_save_button(mouse_x, mouse_y)
            self.print_text_input(input_text)
            ret, save = self.__check_action(button1, mouse_x, mouse_y)
            if save is True and len(input_text) == 0:
                save = False
                ret = False
        return False, ''

    def tmp(self, b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False

    def print_text_input(self, input_text):
        """function for printing text"""
        self.screen.blit(pygame.image.load(RACT_ART), (INPUT_TXT_BAR_X, INPUT_TXT_BAR_Y))
        pygame.display.set_caption('')
        font = pygame.font.Font(None, INPUT_TXT_SIZE)
        text_surface = font.render(input_text, True, INPUT_TXT_COLOR)
        self.screen.blit(text_surface, (INPUT_TXT_X, INPUT_TXT_Y))

    def __check_action(self, button1, mouse_x, mouse_y):
        """function for checking user interactions"""
        if button1 and Object().in_button(mouse_x, mouse_y, Object.SaveNameScr().back_coord()):
            return True, False
        if button1 and Object().in_button(mouse_x, mouse_y, Object.SaveNameScr().save_coord()):
            self.screen.blit(pygame.image.load(VAGNER_ART), (VAGNER_ART_X, VAGNER_ART_Y))
            time.sleep(SLEEP_AFTER_VAGNER)
            return True, True
        return False, False

    def __print_back_button(self, mouse_x, mouse_y):
        """function for printing back button"""
        if Object().in_button(mouse_x, mouse_y, Object.SaveNameScr().back_coord()):
            self.screen.blit(pygame.image.load(BACK_PINK), (Object.SaveNameScr().back_l_c_coord()))
        else:
            self.screen.blit(pygame.image.load(BACK_WHITE), (Object.SaveNameScr().back_l_c_coord()))

    def __print_save_button(self, mouse_x, mouse_y):
        """function for printing save button"""
        if Object().in_button(mouse_x, mouse_y, Object.SaveNameScr().save_coord()):
            self.screen.blit(pygame.image.load(SAVE_PINK), (Object.SaveNameScr().save_l_c_coord()))
        else:
            self.screen.blit(pygame.image.load(SAVE_WHITE), (Object.SaveNameScr().save_l_c_coord()))
