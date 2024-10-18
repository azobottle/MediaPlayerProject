import os
from datetime import datetime

from utils import get_week_range


class Logger:
    def __init__(self):
        self.log_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    def log_playing_file(self, file_path):
        try:
            log_dir = os.path.join("log", get_week_range())
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            with open(os.path.join(log_dir, self.log_filename), 'a', encoding="UTF-8") as log_file:
                log_file.write(f"Playing: {file_path}\n")
            print(f"Logged playing file: {file_path} to {self.log_filename}")
        except Exception as e:
            print(f"Failed to log file: {e}")

custom_logger=Logger()