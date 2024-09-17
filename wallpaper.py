import ctypes
import winreg as reg
import time
from logger import log_playing_file
from gui import pause_event

def set_wallpaper(image_path):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "WallpaperStyle", 0, reg.REG_SZ, "6")  # "6"表示"居中"
        reg.SetValueEx(key, "TileWallpaper", 0, reg.REG_SZ, "0")  # "0"表示不平铺
        reg.CloseKey(key)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")

def play_images(images, log_filename, interval, stop_event):
    index = 0  # 用于追踪当前播放的图片
    while not stop_event.is_set():  # 检查 stop_event 是否已设置
        if pause_event.is_set():  # 检查是否暂停
            log_playing_file(images[index], log_filename)
            set_wallpaper(images[index])
            index = (index + 1) % len(images)  # 循环播放下一张图片
            time.sleep(interval)
        else:
            time.sleep(1)  # 暂停时稍作等待，再次检查是否恢复播放
