import os

from utils import getWeekRange

def log_playing_file(file_path, log_filename):
    try:
        log_dir = os.path.join("log",getWeekRange())
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        with open(os.path.join(log_dir, log_filename), 'a', encoding="UTF-8") as log_file:
            log_file.write(f"Playing: {file_path}\n")
        print(f"Logged playing file: {file_path} to {log_filename}")
    except Exception as e:
        print(f"Failed to log file: {e}")
