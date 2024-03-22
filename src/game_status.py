"""keeping game parameters"""


class Status:
    """class for keeping game parameters"""
    def __init__(self):
        self.conditions = [1, 0]
        self.history_maps = []
        self.user_maps = []
        self.current_map = 0
        self.player_lives = 0

    def get_conditions(self):
        """returns self.coordinates"""
        return self.conditions

    def get_user_maps(self):
        """returns self.user_maps"""
        return self.user_maps
