import os
import time
import ctypes
from pathlib import Path
import winreg as reg
import random
from datetime import datetime

def set_wallpaper(image_path):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "WallpaperStyle", 0, reg.REG_SZ, "6")  # "6"表示"居中"
        reg.SetValueEx(key, "TileWallpaper", 0, reg.REG_SZ, "0")  # "0"表示不平铺
        reg.CloseKey(key)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")

def get_images_from_directory(directory, extensions=['.jpg', '.png', '.bmp']):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(os.path.join(root, file))
    return image_files

def log_playing_file(file_path, log_filename):
    try:
        log_dir = "log"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        with open(os.path.join(log_dir, log_filename), 'a',encoding="UTF-8") as log_file:
            log_file.write(f"Playing: {file_path}\n")
        print(f"Logged playing file: {file_path} to {log_filename}")
    except Exception as e:
        print(f"Failed to log file: {e}")

image_directory = 'D:\MediaPlayerProject\media'  # 确保使用正斜杠或双反斜杠
interval = 10  # 图片轮换的时间间隔（以秒为单位）

images = get_images_from_directory(image_directory)
log_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

if not images:
    print("No images found in the directory.")
else:
    random.shuffle(images)
    
    while True:
        for image in images:
            log_playing_file(image, log_filename)
            set_wallpaper(image)
            time.sleep(interval)
