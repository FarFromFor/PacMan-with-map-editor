"""saving changes and uploading save files"""
import pickle
import os
import config
from game_status import Status


class Upload:
    """class for saving changes and uploading save files"""
    def __init__(self):
        self.status = Status()

    def upload_all(self):
        """function for uploading save files"""
        if os.path.exists(config.SAVE_FILE_NAME):
            with open(config.SAVE_FILE_NAME, "rb") as file:
                self.status = pickle.load(file)
        return self.status

    def save_all(self, status):
        """function for saving changes"""
        with open(config.SAVE_FILE_NAME, "wb") as file:
            pickle.dump(status, file)
