import ctypes
import os
import random
import winreg as reg
import asyncio

from Status import CustomStatus
from logger import file_logger

class ImagePathLoader:
    def __init__(self, directory: str, seed: int):
        self.directory = directory
        self.seed = seed
        self.images = []
        self.set_images_from_directory(directory)
        self.image_index = 0
        self.image_length = len(self.images)

    def next_image_path(self) -> str:
        self.image_index = (self.image_index + 1) % len(self.images)
        return self.images[self.image_index]

    def previous_image_path(self) -> str:
        self.image_index = (self.image_index - 1) % len(self.images)
        return self.images[self.image_index]

    def set_images_from_directory(self, directory, extensions=None):
        if extensions is None:
            extensions = ['.jpg', '.png', '.bmp']
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    self.images.append(os.path.join(root, file))
        random.seed(self.seed)
        random.shuffle(self.images)

class WallPaperChanger:
    def __init__(self, interval: int):
        self.interval = interval

    async def play_images(self, state: CustomStatus, loader: ImagePathLoader):
        path = loader.next_image_path()
        print("[change] first change "+path)
        set_wallpaper(path)
        while True:
            try:
                print("[prepare 1] waiting for re_sleep event or timeout")
                await state.wait_for_re_sleep(self.interval)
            except asyncio.TimeoutError:
                print("[prepare 2] timeout,waiting for Resume value")
                await state.wait_for_value("Resume")
                path = loader.next_image_path()
                print("[change] automatically change "+path)
                set_wallpaper(path)
                print("[end] timeout end")
            else:
                print("[end] re_sleep end,clear to prepare next loop")
                state.clear()  # 清除事件，准备下一次等待

def set_wallpaper(image_path):
    try:
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, reg.KEY_SET_VALUE)
        reg.SetValueEx(key, "WallpaperStyle", 0, reg.REG_SZ, "6")  # "6"表示"居中"
        reg.SetValueEx(key, "TileWallpaper", 0, reg.REG_SZ, "0")  # "0"表示不平铺
        reg.CloseKey(key)

        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        file_logger.log_playing_file(image_path)

    except Exception as e:
        print(f"[error] Failed to set wallpaper: {e}")
