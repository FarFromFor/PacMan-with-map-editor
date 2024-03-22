"""game sound controls"""
import pygame


class Sound:
    """class for working with game sound"""
    max_vol = 10
    volume = 0.1
    sound_delta = 0.1
    @staticmethod
    def play_action_effect(music, volume):
        """function for playing sound effects"""
        button_click_sound = pygame.mixer.Sound(music)
        button_click_sound.set_volume(volume)
        button_click_sound.play()

    @staticmethod
    def play_background_music(music, volume):
        """function for playing background music"""
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(0.1 * volume)
        pygame.mixer.music.play()

    @staticmethod
    def background_music_off():
        """function for turning off background music"""
        pygame.mixer.music.set_volume(0)
