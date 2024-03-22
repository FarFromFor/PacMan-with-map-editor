"""game configurations and constants"""

# MENU CONSTANTS
SIGN = '0.2.9 by Aleksandr Riabov'
PLAY_BLACK = './arts/play_black.png'
PLAY_WHITE = './arts/play_white.png'
CREATE_LVL_BLACK = './arts/create_level_black.png'
CREATE_LVL_WHITE = './arts/create_level_white.png'
PLAY_USER_MAP_BLACK = './arts/play_user_map_black.png'
PLAY_USER_MAP_WHITE = 'arts/play_user_map_white.png'
OPTIONS_BLACK = './arts/options_black.png'
OPTIONS_WHITE = './arts/options_white.png'
EXIT_BLACK = './arts/exit_black.png'
EXIT_WHITE = './arts/exit_white.png'
WAY_L_R = 1
WAY_R_L = 2
TOP_SCREEN = 0
BOTTOM_SCREEN = 760
MIN_SPEED = 3
MAX_SPEED = 6
LEFT_BORDER = -30
RIGHT_BORDER = 1020
PLAY = 1
CREATE_LEVEL = 2
PLAY_USER_MAP = 3
OPTIONS = 4
EXIT = 5

# OPTIONS CONSTANTS
BACK_PINK = 'arts/back_pink.png'
BACK_WHITE = 'arts/back.png'
VOLUME_P_W = 'arts/volume_p_w.png'
VOLUME_W_P = 'arts/volume_w_p.png'
VOLUME_V_V = 'arts/volume_w_w.png'
DIFFICULTY_P_W = 'arts/difficulty_p_w.png'
DIFFICULTY_W_P = 'arts/difficulty_w_p.png'
DIFFICULTY_W_W = 'arts/difficulty_w_w.png'
ZERO_ART = 'arts/numbers/zero.png'
ONE_ART = 'arts/numbers/one.png'
TWO_ART = 'arts/numbers/two.png'
THREE_ART = 'arts/numbers/three.png'
FOUR_ART = 'arts/numbers/four.png'
FIVE_ART = 'arts/numbers/five.png'

# PLAY USER MAP CONSTANTS
TIME_1 = 'arts/time_1.png'
TIME_2 = 'arts/time_2.png'
TIME_3 = 'arts/time_3.png'
TIME_GO = 'arts/time_go.png'
SWITCH_LEFT_PINK = 'arts/switch_left_pink.png'
SWITCH_LEFT_WHITE = 'arts/switch_left.png'
SWITCH_RIGHT_PINK = 'arts/switch_right_pink.png'
SWITCH_RIGHT_WHITE = 'arts/switch_right.png'
DELETE_RED = 'arts/delete_red.png'
DELETE_WHITE = 'arts/delete.png'
PLAY_SMALL_PINK = 'arts/play_pink.png'
PLAY_SMALL_WHITE = 'arts/play.png'
GAME_OVER = './arts/game_over.png'
VICTORY = './arts/victory.png'

# GAME PARAMETERS CONSTANTS
NAME_OF_GAME = 'Pacman'
PACMAN_ARTS_AMOUNT = 18
PLAYER_LIVES = 3
SMALL_BALL_SCORE = 10
BIG_BALL_SCORE = 200
GHOST_SCORE = 200
TIME_WAIT = 0.5
FPS_LOCK = 0.01
COMPANY_MAPS_AMOUNT = 4
VERSION_X = 800
VERSION_Y = 770
VERSION_DONT_SIZE = 20
MAX_TXT_INPUT_LEN = 11
SLEEP_AFTER_SAVE = 0.7
VAGNER_ART_X = 0
VAGNER_ART_Y = 620
SLEEP_AFTER_VAGNER = 0.1
GHOST_SLEEP_TIME = 5
GHOST_SPEED_IN_SLEEP = 1
EASY = 1
MEDIUM = 2
HARD = 3
EASY_GHOST_SPEED = 2
EASY_PACMAN_SPEED = 2
MEDIUM_GHOST_SPEED = 4
MEDIUM_PACMAN_SPEED = 4
HARD_GHOST_SPEED = 5
HARD_PACMAN_SPEED = 4
SLEEP_AFTER_RESTART = 2
SLEEP_AFTER_FINISH = 3
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
DEG_LEFT = 180
DEG_DOWN = 270
DEG_UP = 90

# TEXT PARAMETERS CONSTANTS
INPUT_TXT_SIZE = 65
INPUT_TXT_COLOR = 'pink'
INPUT_TXT_X = 304
INPUT_TXT_Y = 218
INPUT_TXT_BAR_X = 0
INPUT_TXT_BAR_Y = 180
INPUT_TXT_BAR_NAME = ''
SCORE_LIVES_TEXT_SIZE = 40
SCORE = 'SCORE:'
LIVES = 'LIVES:'
SCORE_LIVES_COLOR = 'white'

# lines parameters:
TEXT_X = 5
LIVES_Y = 5
LIVES_AMOUNT_Y = 35
SCORE_Y = 70
SCORE_AMOUNT_Y = 100

# COLORS CONSTANTS
BACKGROUND_COLOR = 'black'
BLOCK_BORDER_COLOR = 'grey'
SMALL_BALL_COLOR = 'white'
BIG_BALL_COLOR = 'white'
VERSION_COLOR = 'grey'

# MAP PARAMETERS CONSTANTS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
BLOCK_SIZE = 40
HALF_B_S = BLOCK_SIZE / 2
DELTA = 3
NO_OBJECT = -1
PANEL_WIDTH = 2
PANEL_HEIGHT = 15
BLOCK_BORDER = 1
SMALL_BALL_R = 5
BIG_BALL_R = 12

# UPLOAD CONSTANTS
SAVE_FILE_NAME = "current_status.pkl"

# MAP OBJECT CONSTANTS
PACMAN_ART = 'arts/live.png'
TOMB_ART = 'arts/tomb.png'
GHOST_RED_ART = 'arts/ghost_red.png'
GHOST_GREEN_ART = 'arts/ghost_green.png'
GHOST_BLUE_ART = 'arts/ghost_blue.png'
GHOST_YELLOW_ART = 'arts/ghost_yellow.png'
GHOST_DOWN_ART = 'arts/ghost_down.png'
DISC_ART = 'arts/disc.png'
RETRY_ART = 'arts/retry_icon.png'
ESC_ART = 'arts/esc_icon.png'

OUT_OF_MAP = -1
EMPTY_BLOCK = 0
WALL = 1
SMALL_BALL = 2
BIG_BALL = 3
LIVE = 4

TOMB = 5
GHOST_RED = 6
GHOST_GREEN = 7
GHOST_BLUE = 8
GHOST_YELLOW = 9

SAVE_ICON = 10
RETRY_ICON = 11
ESC_ICON = 12

PURPLE = 20
MAGENTA = 21
BLUE = 22
GRAY = 23
CYAN = 24
WHITE = 25
GREEN = 26
BROWN = 27
YELLOW = 28
ORANGE = 29
RED = 30
PINK = 31
BLACK = 32

COLORS = ['black'] * 50
COLORS[20] = 'purple'
COLORS[21] = 'magenta'
COLORS[22] = 'blue'
COLORS[23] = 'gray'
COLORS[24] = 'cyan'
COLORS[25] = 'white'
COLORS[26] = 'green'
COLORS[27] = 'brown'
COLORS[28] = 'yellow'
COLORS[29] = 'orange'
COLORS[30] = 'red'
COLORS[31] = 'pink'

# SAVE NAME SCREEN CONSTANTS
VAGNER_ART = 'arts/vagner.png'
SAVE_PINK = 'arts/save_pink.png'
SAVE_WHITE = 'arts/save.png'
RACT_ART = 'arts/ract.png'

# MUSIC CONSTANTS
TICK = 'sounds/tick.mp3'
TOCK = 'sounds/tock.mp3'
LEVEL_0_MUSIC = 'sounds/level_0.mp3'
LEVEL_1_MUSIC = 'sounds/level_1.mp3'
LEVEL_2_MUSIC = 'sounds/level_2.mp3'
LEVEL_3_MUSIC = 'sounds/level_3.mp3'
DIE_SOUND = 'sounds/die_sound_3.mp3'
GAME_OVER_SOUND = 'sounds/game_over_sound.mp3'
WIN_SOUND = 'sounds/win_sound.mp3'
GHOST_EATEN = 'sounds/ghost_eaten.mp3'
USER_MAP_MUSIC = 'sounds/user_map_music.mp3'
MENU_MUSIC = 'sounds/music.mp3'
CLICK = 'sounds/click.wav'
SMALL_BALL_SOUND = 'sounds/click.wav'
BIG_BALL_SOUND = 'sounds/big_ball.mp3'
TOASTY = 'sounds/toasty.wav'


class Object:
    """class consists objects coordinates and functions for them"""
    class Menu:
        """class consists menu objects coordinates and functions for them"""
        def __init__(self):
            self.button1 = {
                'x1': 240,
                'y1': 40,
                'x2': 760,
                'y2': 160,
            }

            self.button2 = {
                'x1': 240,
                'y1': 180,
                'x2': 760,
                'y2': 300
            }

            self.button3 = {
                'x1': 240,
                'y1': 320,
                'x2': 760,
                'y2': 440
            }

            self.button4 = {
                'x1': 240,
                'y1': 460,
                'x2': 760,
                'y2': 580
            }

            self.button5 = {
                'x1': 240,
                'y1': 600,
                'x2': 760,
                'y2': 720
            }

        def button1_coordinates(self):
            """returns button1 coordinates"""
            return [self.button1['x1'], self.button1['y1'], self.button1['x2'], self.button1['y2']]

        def button1_l_c_coord(self):
            """returns button1 left corner coordinates"""
            return [self.button1['x1'], self.button1['y1']]

        def button2_coordinates(self):
            """returns button2 coordinates"""
            return [self.button2['x1'], self.button2['y1'], self.button2['x2'], self.button2['y2']]

        def button2_l_c_coord(self):
            """returns button2 left corner coordinates"""
            return [self.button2['x1'], self.button2['y1']]

        def button3_coordinates(self):
            """returns button3 coordinates"""
            return [self.button3['x1'], self.button3['y1'], self.button3['x2'], self.button3['y2']]

        def button3_l_c_coord(self):
            """returns button3 left corner coordinates"""
            return [self.button3['x1'], self.button3['y1']]

        def button4_coordinates(self):
            """returns button4 coordinates"""
            return [self.button4['x1'], self.button4['y1'], self.button4['x2'], self.button4['y2']]

        def button4_l_c_coord(self):
            """returns button4 left corner coordinates"""
            return [self.button4['x1'], self.button4['y1']]

        def button5_coordinates(self):
            """returns button5 coordinates"""
            return [self.button5['x1'], self.button5['y1'], self.button5['x2'], self.button5['y2']]

        def button5_l_c_coord(self):
            """returns button5 left corner coordinates"""
            return [self.button5['x1'], self.button5['y1']]

    class Options:
        """class consists options objects coordinates and functions for them"""
        def __init__(self):
            self.diff_mi = {
                'x1': 815,
                'y1': 85,
                'x2': 855,
                'y2': 125
            }

            self.diff_pl = {
                'x1': 670,
                'y1': 85,
                'x2': 710,
                'y2': 125
            }

            self.diff_number = {
                'x1': 746,
                'y1': 85,
            }

            self.vol_mi = {
                'x1': 815,
                'y1': 225,
                'x2': 855,
                'y2': 265
            }

            self.vol_pl = {
                'x1': 670,
                'y1': 225,
                'x2': 710,
                'y2': 265
            }

            self.volume_number = {
                'x1': 746,
                'y1': 225,
            }

            self.back = {
                'x1': 417,
                'y1': 600,
                'x2': 583,
                'y2': 653
            }

        def diff_coord(self):
            """returns difficulty panel coordinates"""
            return [0, 40]

        def diff_mi_coord(self):
            """returns difficulty panel minus coordinates"""
            return [self.diff_mi['x1'], self.diff_mi['y1'], self.diff_mi['x2'], self.diff_mi['y2']]

        def diff_pl_coord(self):
            """returns difficulty panel plus coordinates"""
            return [self.diff_pl['x1'], self.diff_pl['y1'], self.diff_pl['x2'], self.diff_pl['y2']]

        def diff_num_coord(self):
            """returns difficulty panel number coordinates"""
            return [self.diff_number['x1'], self.diff_number['y1']]

        def vol_coord(self):
            """returns volume panel minus coordinates"""
            return [0, 180]

        def vol_min_coord(self):
            """returns volume panel minus coordinates"""
            return [self.vol_mi['x1'], self.vol_mi['y1'], self.vol_mi['x2'], self.vol_mi['y2']]

        def vol_pl_coord(self):
            """returns volume panel plus coordinates"""
            return [self.vol_pl['x1'], self.vol_pl['y1'], self.vol_pl['x2'], self.vol_pl['y2']]

        def vol_number_coord(self):
            """returns volume panel number coordinates"""
            return [self.volume_number['x1'], self.volume_number['y1']]

        def back_coordinates(self):
            """returns back button coordinates"""
            return [self.back['x1'], self.back['y1'], self.back['x2'], self.back['y2']]

        def back_l_c_coord(self):
            """returns back button left corner coordinates"""
            return [self.back['x1'], self.back['y1']]

    class SaveNameScr:
        """class consists save name screen objects coordinates and functions for them"""
        def __init__(self):
            self.back = {
                'x1': 417,
                'y1': 600,
                'x2': 583,
                'y2': 653
            }
            self.save = {
                'x1': 423,
                'y1': 350,
                'x2': 589,
                'y2': 403
            }

        def back_coord(self):
            """returns back button coordinates"""
            return [self.back['x1'], self.back['y1'], self.back['x2'], self.back['y2']]

        def back_l_c_coord(self):
            """returns back button left corner coordinates"""
            return [self.back['x1'], self.back['y1']]

        def save_coord(self):
            """returns save button coordinates"""
            return [self.save['x1'], self.save['y1'], self.save['x2'], self.save['y2']]

        def save_l_c_coord(self):
            """returns save button left corner coordinates"""
            return [self.save['x1'], self.save['y1']]

    class PlayUserMapScr:
        """class consists play user map screen objects coordinates and functions for them"""
        def __init__(self):
            self.time = {
                'x1': 440,
                'y1': 340,
                'x2': 560,
                'y2': 460
            }

            self.back = {
                'x1': 417,
                'y1': 600,
                'x2': 583,
                'y2': 653
            }
            self.play = {
                'x1': 423,
                'y1': 350,
                'x2': 589,
                'y2': 403
            }
            self.delete = {
                'x1': 385,
                'y1': 450,
                'x2': 625,
                'y2': 490
            }
            self.sw_l = {
                'x1': 150,
                'y1': 197,
                'x2': 220,
                'y2': 281
            }
            self.sw_r = {
                'x1': 780,
                'y1': 197,
                'x2': 850,
                'y2': 281
            }

        def time_c_coord(self):
            """returns time left corner coordinates"""
            return [self.time['x1'], self.time['y1']]

        def del_coord(self):
            """returns delete button coordinates"""
            return [self.delete['x1'], self.delete['y1'], self.delete['x2'], self.delete['y2']]

        def delete_left_corner_coordinates(self):
            """returns delete button left corner coordinates"""
            return [self.delete['x1'], self.delete['y1']]

        def sw_r_coord(self):
            """returns switch right coordinates"""
            return [self.sw_r['x1'], self.sw_r['y1'], self.sw_r['x2'], self.sw_r['y2']]

        def switch_right_left_corner_coordinates(self):
            """returns switch right left corner coordinates"""
            return [self.sw_r['x1'], self.sw_r['y1']]

        def sw_l_coord(self):
            """returns switch left coordinates"""
            return [self.sw_l['x1'], self.sw_l['y1'], self.sw_l['x2'], self.sw_l['y2']]

        def sw_l_l_cor_coord(self):
            """returns switch left left corner coordinates"""
            return [self.sw_l['x1'], self.sw_l['y1']]

        def back_coord(self):
            """returns back button coordinates"""
            return [self.back['x1'], self.back['y1'], self.back['x2'], self.back['y2']]

        def back_left_corner_coordinates(self):
            """returns back button left corner coordinates"""
            return [self.back['x1'], self.back['y1']]

        def play_coord(self):
            """returns play button coordinates"""
            return [self.play['x1'], self.play['y1'], self.play['x2'], self.play['y2']]

        def play_left_corner_coordinates(self):
            """returns play button left corner coordinates"""
            return [self.play['x1'], self.play['y1']]

    class EndOfGame:
        """class end of game objects coordinates and functions for them"""
        def __init__(self):
            self.end_sgn = {
                'x1': 240,
                'y1': 280,
                'x2': 760,
                'y2': 400
            }

        def end_sign_coordinates(self):
            """returns end sign coordinates"""
            return [self.end_sgn['x1'], self.end_sgn['y1'], self.end_sgn['x2'], self.end_sgn['y2']]

        def end_sign_corner_coordinates(self):
            """returns end sign left corner coordinates"""
            return [self.end_sgn['x1'], self.end_sgn['y1']]

    def not_in_button(self, mouse_x, mouse_y, coord):
        """returns true if mouse coordinates are not in coord"""
        if coord[0] <= mouse_x <= coord[2] and coord[1] <= mouse_y <= coord[3]:
            return False
        return True

    def in_button(self, mouse_x, mouse_y, coord):
        """returns true if mouse coordinates are in coord"""
        if coord[0] <= mouse_x <= coord[2] and coord[1] <= mouse_y <= coord[3]:
            return True
        return False


class MapObject:
    """class for working with map objects"""
    @staticmethod
    def is_ghost(obj):
        """returns true if obj is a ghost"""
        if 5 < obj < 10:
            return True
        return False

    @staticmethod
    def is_ball(obj):
        """returns true if obj is a ball"""
        if obj in (2, 3):
            return True
        return False

    @staticmethod
    def is_wall(obj):
        """returns true if obj is a wall"""
        if 20 <= obj <= 31:
            return True
        return False
