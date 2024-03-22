"""playing selected map"""

import time
import copy
import random
import pygame
from sounds import Sound
from config import *


class Character:
    """classs for representing characters: pacman and ghosts"""
    def __init__(self, x, y, identity):
        self.map_x = round(x / BLOCK_SIZE)
        self.map_y = round(y / BLOCK_SIZE)
        # UP - 0, RIGHT - 1, DOWN - 2, LEFT - 3
        self.direction = UP
        self.x = x
        self.y = y
        self.default_params = {"def_x": x, "def_y": y, "speed_def": 0, "id": identity, "speed": 0}
        self.current_params = {"dead": False, "down": False, "c_time": time.time()}

    def go(self):
        """move character in its direction"""
        if self.direction == UP:
            self.y -= self.default_params["speed"]
        elif self.direction == RIGHT:
            self.x += self.default_params["speed"]
        elif self.direction == DOWN:
            self.y += self.default_params["speed"]
        elif self.direction == LEFT:
            self.x -= self.default_params["speed"]
        self.map_x = round(self.x / BLOCK_SIZE)
        self.map_y = round(self.y / BLOCK_SIZE)
        if self.current_params["c_time"] <= time.time() and self.current_params["down"]:
            self.up()

    def up(self):
        """function for waking up ghosts"""
        if self.current_params["dead"]:
            self.current_params["dead"] = False
            self.set_default()
        self.current_params["down"] = False
        self.x = self.map_x * BLOCK_SIZE
        self.y = self.map_y * BLOCK_SIZE
        if self.default_params["speed"] < self.default_params["speed_def"]:
            self.default_params["speed"] = self.default_params["speed_def"]

    def down(self):
        """function for making ghosts 'sleep'"""
        self.current_params["c_time"] = time.time() + GHOST_SLEEP_TIME
        self.current_params["down"] = True
        if self.default_params["speed"] > self.default_params["speed_def"]:
            self.default_params["speed_def"] = self.default_params["speed"]
        self.default_params["speed"] = GHOST_SPEED_IN_SLEEP

    def set_default(self):
        """returns a character to its start position"""
        self.x = self.default_params["def_x"]
        self.y = self.default_params["def_y"]
        self.map_x = round(self.x / BLOCK_SIZE)
        self.map_y = round(self.y / BLOCK_SIZE)

    def turn_right(self):
        """turns character right"""
        self.direction += 1
        self.direction %= 4

    def turn_around(self):
        """turns character around"""
        self.turn_right()
        self.turn_right()


class Play:
    """class playing selected map"""
    def __init__(self, screen, status, map_to_play):
        self.screen = screen
        self.game_map = copy.deepcopy(map_to_play)

        self.game_params = {"win": False,
                            "lose": False,
                            "balls": 0,
                            "count": 0,
                            "change": -1,
                            "lives": PLAYER_LIVES,
                            "score": 0}

        self.chars = self.__create_characters()
        self.__balls_counter()
        self.__set_difficulty(status.conditions)

    def __balls_counter(self):
        """function for counting all the balls on the map"""
        for row in range(self.screen.get_height() // BLOCK_SIZE):
            for col in range(self.screen.get_width() // BLOCK_SIZE):
                if MapObject.is_ball(self.game_map[row][col]):
                    self.game_params["balls"] += 1

    def __set_difficulty(self, conditions):
        """set speed for pacman and ghosts according to selected difficulty"""
        if conditions[0] == EASY:
            self.chars["pm"].default_params["speed"] = EASY_PACMAN_SPEED
            self.chars["gr"].default_params["speed"] = EASY_GHOST_SPEED
            self.chars["gb"].default_params["speed"] = EASY_GHOST_SPEED
            self.chars["gg"].default_params["speed"] = EASY_GHOST_SPEED
            self.chars["gy"].default_params["speed"] = EASY_GHOST_SPEED
        elif conditions[0] == MEDIUM:
            self.chars["pm"].default_params["speed"] = MEDIUM_PACMAN_SPEED
            self.chars["gr"].default_params["speed"] = MEDIUM_GHOST_SPEED
            self.chars["gb"].default_params["speed"] = MEDIUM_GHOST_SPEED
            self.chars["gg"].default_params["speed"] = MEDIUM_GHOST_SPEED
            self.chars["gy"].default_params["speed"] = MEDIUM_GHOST_SPEED
        elif conditions[0] == HARD:
            self.chars["pm"].default_params["speed"] = HARD_PACMAN_SPEED
            self.chars["gr"].default_params["speed"] = HARD_GHOST_SPEED
            self.chars["gb"].default_params["speed"] = HARD_GHOST_SPEED
            self.chars["gg"].default_params["speed"] = HARD_GHOST_SPEED
            self.chars["gy"].default_params["speed"] = HARD_GHOST_SPEED

    def __create_characters(self):
        """function to creating characters"""
        player_x, player_y = self.__get_object_coordinates(LIVE)
        packman = Character(player_x, player_y, LIVE)

        ghost_x, ghost_y = self.__get_object_coordinates(GHOST_RED)
        ghost_red = Character(ghost_x, ghost_y, GHOST_RED)

        ghost_x, ghost_y = self.__get_object_coordinates(GHOST_BLUE)
        ghost_blue = Character(ghost_x, ghost_y, GHOST_BLUE)

        ghost_x, ghost_y = self.__get_object_coordinates(GHOST_GREEN)
        ghost_green = Character(ghost_x, ghost_y, GHOST_GREEN)

        ghost_x, ghost_y = self.__get_object_coordinates(GHOST_YELLOW)
        ghost_yellow = Character(ghost_x, ghost_y, GHOST_YELLOW)

        chars = {"pm": packman,
                 "gr": ghost_red,
                 "gb": ghost_blue,
                 "gg": ghost_green,
                 "gy": ghost_yellow}
        return chars

    def play_map(self, screen):
        """function for playing the map"""
        run = True
        pl = True
        while run:
            self.__print_text()
            time.sleep(FPS_LOCK)
            pygame.display.update()
            screen.fill(pygame.Color(BACKGROUND_COLOR))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return False

            # If commands were entered
            mouse_x, mouse_y = pygame.mouse.get_pos()
            button1, button2, button3 = pygame.mouse.get_pressed()
            mouse_row = mouse_y // BLOCK_SIZE
            mouse_col = mouse_x // BLOCK_SIZE

            if button1 and self.game_map[mouse_row][mouse_col] == ESC_ICON:
                Sound().play_action_effect(CLICK, Sound.volume)
                return False

            # Drawing objects
            for row in range(self.screen.get_height() // BLOCK_SIZE):
                for col in range(self.screen.get_width() // BLOCK_SIZE):
                    self.__print_object(row, col, col * BLOCK_SIZE, row * BLOCK_SIZE)
            self.__packman_move()
            self.__check_contact()
            self.__draw_player()
            self.__ghost_move(self.chars["gr"])
            self.__ghost_move(self.chars["gb"])
            self.__ghost_move(self.chars["gg"])
            self.__ghost_move(self.chars["gy"])
            self.__draw_ghost(self.chars["gr"])
            self.__draw_ghost(self.chars["gb"])
            self.__draw_ghost(self.chars["gg"])
            self.__draw_ghost(self.chars["gy"])
            self.__check_win_or_lose()
            self.dumm(button2, button3)
            if pl:
                self.__before_start_timer()
                pl = False
            if self.game_params["win"]:
                self.__win()
                return True
            if self.game_params["lose"]:
                self.__game_over()
                return False
        return False

    def __before_start_timer(self):
        """function for count down"""
        self.screen.blit(pygame.image.load(TIME_3), (Object.PlayUserMapScr().time_c_coord()))
        Sound().play_action_effect(TICK, Sound.volume * Sound.max_vol)
        pygame.display.update()
        time.sleep(TIME_WAIT)

        self.screen.blit(pygame.image.load(TIME_2), (Object.PlayUserMapScr().time_c_coord()))
        Sound().play_action_effect(TICK, Sound.volume * Sound.max_vol)
        pygame.display.update()
        time.sleep(TIME_WAIT)

        self.screen.blit(pygame.image.load(TIME_1), (Object.PlayUserMapScr().time_c_coord()))
        Sound().play_action_effect(TICK, Sound.volume * Sound.max_vol)
        pygame.display.update()
        time.sleep(TIME_WAIT)

        self.screen.blit(pygame.image.load(TIME_GO), (Object.PlayUserMapScr().time_c_coord()))
        Sound().play_action_effect(TICK, Sound.volume * Sound.max_vol)
        pygame.display.update()
        time.sleep(TIME_WAIT)

    def __restart(self):
        """returns all characters on their start position and decreases lives amount"""
        self.chars["pm"].set_default()
        self.chars["gr"].set_default()
        self.chars["gb"].set_default()
        self.chars["gg"].set_default()
        self.chars["gy"].set_default()
        self.game_params["lives"] -= 1
        time.sleep(SLEEP_AFTER_RESTART)

    def __game_over(self):
        """function for finishing the game in case of lose"""
        self.screen.blit(pygame.image.load(GAME_OVER),
                         (Object.EndOfGame().end_sign_corner_coordinates()))
        Sound.background_music_off()
        Sound().play_action_effect(GAME_OVER_SOUND, Sound.volume)
        pygame.display.update()
        time.sleep(SLEEP_AFTER_FINISH)

    def dumm(self, b2, b3):
        """dummy function"""
        if b2 == b3:
            return True
        return False

    def __win(self):
        """function for finishing the game in case of winning"""
        self.screen.blit(pygame.image.load(VICTORY),
                         (Object.EndOfGame().end_sign_corner_coordinates()))
        Sound.background_music_off()
        Sound().play_action_effect(WIN_SOUND, Sound.volume)
        pygame.display.update()
        time.sleep(SLEEP_AFTER_FINISH)

    def __check_win_or_lose(self):
        """function for checking if win or lose happened"""
        if self.game_params["lives"] <= 0:
            self.game_params["lose"] = True
        if self.game_params["balls"] == 0:
            self.game_params["win"] = True

    def __ghost_move(self, ghost):
        """function for moving ghosts"""
        ghost.direction = self.__check_open_way(ghost)
        if not self.__is_collision(ghost):
            ghost.go()
        else:
            ghost.turn_around()
            ghost.go()

    def __check_open_way(self, ghost):
        """function for checking open ways for ghost in current position"""
        dirs = []
        if not self.__is_collision(ghost):
            dirs.append(ghost.direction)
        ghost.turn_right()
        if not self.__is_collision(ghost):
            dirs.append(ghost.direction)
        ghost.turn_around()
        if not self.__is_collision(ghost):
            dirs.append(ghost.direction)
        if len(dirs) == 0:
            ghost.turn_around()
            ghost.turn_right()
            dirs.append(ghost.direction)
        return random.choice(dirs)

    def __packman_move(self):
        """function for moving pacman in its curren direction"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.game_params["change"] = UP
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.game_params["change"] = RIGHT
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.game_params["change"] = DOWN
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.game_params["change"] = LEFT

        tmp = self.chars["pm"].direction
        self.chars["pm"].direction = self.game_params["change"]
        if self.__is_collision(self.chars["pm"]):
            self.chars["pm"].direction = tmp
        if not self.__is_collision(self.chars["pm"]):
            self.chars["pm"].go()

    def __print_text(self):
        """function for printing score and lives text"""
        pygame.display.set_caption('')
        font = pygame.font.Font(None, SCORE_LIVES_TEXT_SIZE)
        text_surface = font.render(LIVES, True, SCORE_LIVES_COLOR)
        self.screen.blit(text_surface, (TEXT_X, LIVES_Y))
        text_surface = font.render(str(self.game_params["lives"]), True, SCORE_LIVES_COLOR)
        self.screen.blit(text_surface, (TEXT_X, LIVES_AMOUNT_Y))
        text_surface = font.render(SCORE, True, SCORE_LIVES_COLOR)
        self.screen.blit(text_surface, (TEXT_X, SCORE_Y))
        text_surface = font.render(str(self.game_params["score"]), True, SCORE_LIVES_COLOR)
        self.screen.blit(text_surface, (TEXT_X, SCORE_AMOUNT_Y))

    def __check_contact(self):
        """functions for checking contact with ghosts and balls"""
        def __check_contact_ghost(ghost):
            """functions for checking contact with ghosts"""
            if ghost.map_y == self.chars["pm"].map_y and ghost.map_x == self.chars["pm"].map_x:
                if ghost.current_params["dead"]:
                    return
                if ghost.current_params["down"] and not ghost.current_params["dead"]:
                    Sound().play_action_effect(GHOST_EATEN, Sound.volume)
                    ghost.current_params["dead"] = True
                    self.game_params["score"] += GHOST_SCORE
                else:
                    Sound().play_action_effect(DIE_SOUND, Sound.volume)
                    self.game_params["change"] = -1
                    self.__restart()

        if self.game_map[self.chars["pm"].map_y][self.chars["pm"].map_x] == SMALL_BALL:
            self.game_params["score"] += SMALL_BALL_SCORE
            self.game_params["balls"] -= 1
            Sound().play_action_effect(SMALL_BALL_SOUND, Sound.volume)
            self.game_map[self.chars["pm"].map_y][self.chars["pm"].map_x] = BLACK
        elif self.game_map[self.chars["pm"].map_y][self.chars["pm"].map_x] == BIG_BALL:
            self.chars["gr"].down()
            self.chars["gb"].down()
            self.chars["gg"].down()
            self.chars["gy"].down()
            self.game_params["score"] += BIG_BALL_SCORE
            self.game_params["balls"] -= 1
            Sound().play_action_effect(BIG_BALL_SOUND, Sound.volume)
            self.game_map[self.chars["pm"].map_y][self.chars["pm"].map_x] = BLACK

        __check_contact_ghost(self.chars["gr"])
        __check_contact_ghost(self.chars["gb"])
        __check_contact_ghost(self.chars["gg"])
        __check_contact_ghost(self.chars["gy"])

    def __is_collision(self, packman):
        """function for checking collisions with walls and map borders"""
        if self.__check_collision_contact(packman):
            return True
        if self.__check_collision_border(packman):
            return True
        return False

    def __check_collision_contact(self, pacman):
        """function for checking collisions with walls"""
        bs = BLOCK_SIZE
        y_min_speed = pacman.y - pacman.default_params["speed"]
        x_min_speed = pacman.x - pacman.default_params["speed"]
        up_is_wall = MapObject.is_wall(self.game_map[y_min_speed // bs][pacman.map_x])
        right_is_wall = MapObject.is_wall(self.game_map[pacman.map_y][pacman.x // bs + 1])
        down_is_wall = MapObject.is_wall(self.game_map[pacman.y // bs + 1][pacman.map_x])
        left_is_wall = MapObject.is_wall(self.game_map[pacman.map_y][x_min_speed // bs])
        if pacman.direction == DOWN and pacman.y // bs + 1 >= 20 or pacman.map_x >= 25:
            return True
        if pacman.direction == UP and ((pacman.x % bs != 0) or up_is_wall):
            return True
        if pacman.direction == RIGHT and ((pacman.y % bs != 0) or right_is_wall):
            return True
        if pacman.direction == DOWN and ((pacman.x % bs != 0) or down_is_wall):
            return True
        if pacman.direction == LEFT and ((pacman.y % bs != 0) or left_is_wall):
            return True
        return False

    def __check_collision_border(self, pacman):
        """function for checking collisions with map borders"""
        bs = BLOCK_SIZE
        if pacman.direction == UP and (pacman.y - pacman.default_params["speed"]) // bs < 0:
            return True
        if pacman.direction == RIGHT and pacman.x // bs + 1 >= 22:
            return True
        if pacman.direction == DOWN and pacman.y // bs + 1 >= 20:
            return True
        if pacman.direction == LEFT and (pacman.x - pacman.default_params["speed"]) // bs + 1 < 4:
            return True
        return False

    def __draw_ghost(self, ghost):
        """function for drawing the ghost according to its coordinates"""
        if ghost.current_params["dead"]:
            return
        if ghost.current_params["down"]:
            self.screen.blit(pygame.image.load(GHOST_DOWN_ART), (ghost.x, ghost.y))
            return
        if ghost.default_params["id"] == GHOST_RED:
            self.screen.blit(pygame.image.load(GHOST_RED_ART), (ghost.x, ghost.y))
        elif ghost.default_params["id"] == GHOST_BLUE:
            self.screen.blit(pygame.image.load(GHOST_BLUE_ART), (ghost.x, ghost.y))
        elif ghost.default_params["id"] == GHOST_GREEN:
            self.screen.blit(pygame.image.load(GHOST_GREEN_ART), (ghost.x, ghost.y))
        elif ghost.default_params["id"] == GHOST_YELLOW:
            self.screen.blit(pygame.image.load(GHOST_YELLOW_ART), (ghost.x, ghost.y))

    def __draw_player(self):
        """function for drawing the pacman according to its coordinates"""
        self.game_params["count"] %= PACMAN_ARTS_AMOUNT
        self.game_params["count"] += 1
        img = pygame.image.load(f'arts/pacman/p{self.game_params["count"]}.png')
        if self.chars["pm"].direction == LEFT:
            self.screen.blit(pygame.transform.rotate(img, DEG_LEFT),
                             (self.chars["pm"].x, self.chars["pm"].y))
        elif self.chars["pm"].direction == DOWN:
            self.screen.blit(pygame.transform.rotate(img, DEG_DOWN),
                             (self.chars["pm"].x, self.chars["pm"].y))
        elif self.chars["pm"].direction == UP:
            self.screen.blit(pygame.transform.rotate(img, DEG_UP),
                             (self.chars["pm"].x, self.chars["pm"].y))
        else:
            self.screen.blit(img, (self.chars["pm"].x, self.chars["pm"].y))

    def __get_object_coordinates(self, obj):
        """function for getting obj coordinates on the map"""
        for row in range(self.screen.get_height() // BLOCK_SIZE):
            for col in range(self.screen.get_width() // BLOCK_SIZE):
                if self.game_map[row][col] == obj:
                    if MapObject.is_ghost(obj):
                        self.game_map[row][col] = TOMB
                    else:
                        self.game_map[row][col] = BLACK
                    return col * BLOCK_SIZE, row * BLOCK_SIZE
        return 0, 0

    def __print_object(self, row, col, x, y):
        """function for printing objects on the screen according to its coordinates"""
        draw_obj = {
            TOMB:
                lambda: self.screen.blit(pygame.image.load(TOMB_ART), (x, y)),
            ESC_ICON:
                lambda: self.screen.blit(pygame.image.load(ESC_ART), (x, y)),
            SMALL_BALL:
                lambda: pygame.draw.circle(self.screen, SMALL_BALL_COLOR,
                                           (x + HALF_B_S, y + HALF_B_S), SMALL_BALL_R),
            BIG_BALL:
                lambda: pygame.draw.circle(self.screen, BIG_BALL_COLOR,
                                           (x + HALF_B_S, y + HALF_B_S), BIG_BALL_R)
        }
        draw_obj.get(self.game_map[row][col], lambda: None)()
        if MapObject.is_wall(self.game_map[row][col]):
            pygame.draw.rect(self.screen, pygame.Color(COLORS[self.game_map[row][col]]),
                             (x, y, BLOCK_SIZE, BLOCK_SIZE))
