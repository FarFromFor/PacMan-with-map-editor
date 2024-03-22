"""class for creating a user map"""
import time
import pygame
from save_name_screen import SaveScreen
from sounds import Sound
from config import *


class Creator:
    """class for creating a user map"""
    def __init__(self, screen, conditions):
        self.screen = screen
        self.map_width = screen.get_width() // BLOCK_SIZE
        self.map_height = screen.get_height() // BLOCK_SIZE
        self.game_map = []
        self.conditions = conditions

    def create_map(self):
        """function for creating a user map"""
        self.__fill_map()
        current_object = NO_OBJECT
        run = True
        refresh = False
        while run:
            time.sleep(FPS_LOCK)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False, []
            self.screen.fill(pygame.Color(BACKGROUND_COLOR))
            # If commands were entered
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1, button2, button3 = pygame.mouse.get_pressed()
            mouse_row = mouse_y // BLOCK_SIZE
            mouse_col = mouse_x // BLOCK_SIZE

            if mouse_row < self.map_height and mouse_col < self.map_width:
                if button1 and self.game_map[mouse_row][mouse_col] == SAVE_ICON:
                    Sound().play_action_effect(CLICK, Sound.volume)
                    save, map_name = SaveScreen(self.screen, self.conditions).save()
                    if save:
                        self.__prepare_map()
                        return True, [map_name, self.game_map]
                elif button1 and self.game_map[mouse_row][mouse_col] == ESC_ICON:
                    Sound().play_action_effect(CLICK, Sound.volume)
                    return True, []
                elif button1 and self.game_map[mouse_row][mouse_col] == RETRY_ICON:
                    refresh = True
                elif not button1 and refresh:
                    refresh = False
                    Sound().play_action_effect(CLICK, Sound.volume)
                    self.refresh_map()

            # Writing objects
            current_object = self.__write_objects(current_object)

            # Drawing objects
            self.draw_obj()
            self.dum_f(button2, button3)

        return None

    @staticmethod
    def dum_f(b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False

    def draw_obj(self):
        """function for printing objects"""
        for row in range(self.map_height):
            for col in range(self.map_width):
                x, y = col * BLOCK_SIZE, row * BLOCK_SIZE
                self.__print_object(row, col, x, y)

    def refresh_map(self):
        """function for clearing the map"""
        for row in range(self.map_height):
            for col in range(self.map_width):
                if DELTA <= col < self.map_width - DELTA:
                    self.game_map[row][col] = EMPTY_BLOCK
        print(self.game_map)

    def __write_objects(self, current_object):
        """function for writing objects on map"""
        mouse_x, mouse_y = pygame.mouse.get_pos()
        button1, button2, button3 = pygame.mouse.get_pressed()
        mouse_row = mouse_y // BLOCK_SIZE
        mouse_col = mouse_x // BLOCK_SIZE

        if mouse_row < self.map_height and mouse_col < self.map_width:
            if button1 and mouse_col < PANEL_WIDTH and mouse_row < PANEL_HEIGHT:
                current_object = self.game_map[mouse_row][mouse_col]
            elif button1 and (DELTA <= mouse_col < self.map_width - DELTA):
                self.__check_if_one(current_object)
                self.game_map[mouse_row][mouse_col] = current_object
            elif button3 and (DELTA <= mouse_col < self.map_width - DELTA):
                self.game_map[mouse_row][mouse_col] = EMPTY_BLOCK
            return current_object
        self.dum_f(button2, button3)
        return None

    def __check_if_one(self, obj):
        """function for checking if map consists only one pacman and ghosts icons"""
        for row in range(self.map_height):
            for col in range(self.map_width):
                if DELTA <= col < self.map_width - DELTA:
                    if self.game_map[row][col] == obj and (MapObject.is_ghost(obj) or obj == LIVE):
                        self.game_map[row][col] = EMPTY_BLOCK

    # Print objects on the screen
    def __print_object(self, row, col, x, y):
        """function for printing objects"""
        hb = HALF_B_S
        bs = BLOCK_SIZE
        bbc = BLOCK_BORDER_COLOR
        sm_bc = SMALL_BALL_COLOR
        bg_bc = BIG_BALL_COLOR
        sc = self.screen
        draw_obj = {
            LIVE:
                lambda: self.screen.blit(pygame.image.load(PACMAN_ART), (x, y)),
            TOMB:
                lambda: self.screen.blit(pygame.image.load(TOMB_ART), (x, y)),
            GHOST_RED:
                lambda: self.screen.blit(pygame.image.load(GHOST_RED_ART), (x, y)),
            GHOST_GREEN:
                lambda: self.screen.blit(pygame.image.load(GHOST_GREEN_ART), (x, y)),
            GHOST_BLUE:
                lambda: self.screen.blit(pygame.image.load(GHOST_BLUE_ART), (x, y)),
            GHOST_YELLOW:
                lambda: self.screen.blit(pygame.image.load(GHOST_YELLOW_ART), (x, y)),
            SAVE_ICON:
                lambda: self.screen.blit(pygame.image.load(DISC_ART), (x, y)),
            RETRY_ICON:
                lambda: self.screen.blit(pygame.image.load(RETRY_ART), (x, y)),
            ESC_ICON:
                lambda: self.screen.blit(pygame.image.load(ESC_ART), (x, y)),
            EMPTY_BLOCK:
                lambda: pygame.draw.rect(sc, pygame.Color(bbc), (x, y, bs, bs), BLOCK_BORDER),
            SMALL_BALL:
                lambda: pygame.draw.circle(sc, sm_bc, (x + hb, y + hb), SMALL_BALL_R),
            BIG_BALL:
                lambda: pygame.draw.circle(sc, bg_bc, (x + hb, y + hb), BIG_BALL_R)
        }
        draw_obj.get(self.game_map[row][col], lambda: None)()
        if self.game_map[row][col] is None:
            self.game_map[row][col] = NO_OBJECT
        if MapObject.is_wall(self.game_map[row][col]):
            pygame.draw.rect(sc, pygame.Color(COLORS[self.game_map[row][col]]), (x, y, bs, bs))

    def __prepare_map(self):
        """function for cleaning map of tools before returning"""
        d = DELTA
        for row in range(self.map_height):
            for col in range(self.map_width):
                if d <= col < self.map_width - d and self.game_map[row][col] == EMPTY_BLOCK:
                    self.game_map[row][col] = BLACK
                elif (col < d or col >= self.map_width - d) and self.game_map[row][col] != ESC_ICON:
                    self.game_map[row][col] = BLACK

    # Makes template of map (writing colors and objects, net, options icons ...)
    def __fill_map(self):
        """adds drawing tools and icons"""
        for _ in range(self.map_height):
            line = []
            for col in range(self.map_width):
                if DELTA <= col < self.map_width - DELTA:
                    line.append(EMPTY_BLOCK)
                else:
                    line.append(OUT_OF_MAP)
            self.game_map.append(line)

        self.game_map[0][0] = PURPLE
        self.game_map[0][1] = MAGENTA
        self.game_map[1][0] = BLUE
        self.game_map[1][1] = GRAY
        self.game_map[2][0] = BLACK
        self.game_map[2][1] = WHITE
        self.game_map[3][0] = GREEN
        self.game_map[3][1] = BROWN
        self.game_map[4][0] = YELLOW
        self.game_map[4][1] = ORANGE
        self.game_map[5][0] = RED
        self.game_map[5][1] = CYAN

        self.game_map[6][0] = BIG_BALL
        self.game_map[6][1] = SMALL_BALL
        self.game_map[7][0] = LIVE
        self.game_map[7][1] = GHOST_RED
        self.game_map[8][0] = GHOST_YELLOW
        self.game_map[8][1] = GHOST_GREEN
        self.game_map[9][0] = GHOST_BLUE

        self.game_map[19][23] = SAVE_ICON
        self.game_map[19][24] = RETRY_ICON
        self.game_map[0][24] = ESC_ICON
