import ctypes
import winreg as reg
import time
from logger import log_playing_file
from gui import pause_event
global manual_switch
global next_index
global last_switch_time
manual_switch = False  # 标志是否为手动切换

def set_wallpaper(image_path):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "WallpaperStyle", 0, reg.REG_SZ, "6")  # "6"表示"居中"
        reg.SetValueEx(key, "TileWallpaper", 0, reg.REG_SZ, "0")  # "0"表示不平铺
        reg.CloseKey(key)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    except Exception as e:
        print(f"Failed to set wallpaper: {e}")

def play_images(images, log_filename, interval, stop_event, current_index):
    global manual_switch
    global next_index
    change_image(images,current_index,log_filename)
    while not stop_event.is_set():  # 检查 stop_event 是否已设置
        if pause_event.is_set():  # 检查是否暂停
            current_time = time.time()
            if manual_switch:  # 手动切换
                change_image(images,current_index,log_filename)
                manual_switch = False  # 重置手动切换标志
            elif current_time - last_switch_time >= interval:
                current_index[0]=next_index
                change_image(images,current_index,log_filename)
            time.sleep(1)  # 每秒检查一次
        else:
            time.sleep(1)  # 暂停时稍作等待，再次检查是否恢复播放

def change_image(images,current_index,log_filename):
    global next_index
    global last_switch_time
    log_playing_file(images[current_index[0]], log_filename)
    set_wallpaper(images[current_index[0]])
    next_index=current_index[0]+1
    last_switch_time = time.time()  # 记录上次切换的时间
def change_image_manual(index, images):
    global manual_switch
    manual_switch = True  # 标记为手动切换
    set_wallpaper(images[index])  # 根据索引更改壁纸
