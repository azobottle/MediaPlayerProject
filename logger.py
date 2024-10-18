import os
from datetime import datetime

from utils import get_week_range


class FileLogger:
    def __init__(self):
        self.log_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    def log_playing_file(self, file_path):
        try:
            log_dir = os.path.join("log", get_week_range())
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            with open(os.path.join(log_dir, self.log_filename), 'a', encoding="UTF-8") as log_file:
                log_file.write(f"Playing: {file_path}\n")
        except Exception as e:
            print(e)
            log_file.write(e)

file_logger = FileLogger()