import os
import time
import ctypes
from pathlib import Path
import winreg as reg
import random
from datetime import datetime

# 定义函数来设置壁纸并更新壁纸展示方式（居中显示，不拉伸）
def set_wallpaper(image_path):
    # 设置壁纸的展示样式为"适应屏幕"
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, "WallpaperStyle", 0, reg.REG_SZ, "6")  # "6"表示"居中"
    reg.SetValueEx(key, "TileWallpaper", 0, reg.REG_SZ, "0")  # "0"表示不平铺
    reg.CloseKey(key)

    # 使用 Windows API 设置壁纸
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

# 获取图片目录下的所有图片（包括子目录中的图片）
def get_images_from_directory(directory, extensions=['.jpg', '.png', '.bmp']):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(os.path.join(root, file))
    return image_files

# 记录当前播放的文件路径到日志
def log_playing_file(file_path, log_filename):
    # 打开日志文件并将播放文件路径追加到日志中
    with open("log/"+log_filename, 'a') as log_file:
        log_file.write(f"Playing: {file_path}\n")
    print(f"Logged playing file: {file_path} to {log_filename}")

# 目录路径
image_directory = 'D:\MediaPlayerProject\media'  # 替换为你的图片目录
interval = 10  # 图片轮换的时间间隔（以秒为单位）

# 获取所有图片文件
images = get_images_from_directory(image_directory)
log_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

if not images:
    print("No images found in the directory.")
else:
    # 打乱图片列表
    random.shuffle(images)
    
    # 循环播放图片作为壁纸
    while True:
        for image in images:
            # 记录当前播放的媒体文件路径到日志
            log_playing_file(image, log_filename)
            set_wallpaper(image)  # 设置当前图片为壁纸
            time.sleep(interval)  # 等待一段时间后切换到下一张图片
