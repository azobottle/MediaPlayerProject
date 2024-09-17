import os
import ctypes
import random
import subprocess
from config import media_directory, extensions, video_duration, interval
from logger import log_playing_file

class MediaPlayer:
    def __init__(self):
        self.media_files = self.get_media_from_directory(media_directory)
        self.current_index = 0
        self.is_paused = False
        self.is_looping = True  # 添加循环播放的标志

        # 打乱媒体文件列表
        random.shuffle(self.media_files)

    def get_media_from_directory(self, directory):
        media_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if any(file.lower().endswith(ext) for ext in extensions):
                    media_files.append(os.path.join(root, file))
        return media_files

    def set_wallpaper(self, image_path):
        key = ctypes.windll.user32.SystemParametersInfoW
        key(20, 0, image_path, 3)
        log_playing_file(image_path)

    def play_video_as_wallpaper(self, video_path):
        vlc_command = ['vlc', '--video-wallpaper', '--no-audio', video_path]
        subprocess.Popen(vlc_command)
        log_playing_file(video_path)

    def play_current(self):
        if self.is_paused:
            return
        
        media = self.media_files[self.current_index]
        if media.lower().endswith(('.mp4', '.avi', '.mkv')):
            self.play_video_as_wallpaper(media)
            # 暂时设置播放视频的时长
            time.sleep(video_duration)
        else:
            self.set_wallpaper(media)
            time.sleep(interval)

    def play_next(self):
        if self.is_looping:
            self.current_index = (self.current_index + 1) % len(self.media_files)
        else:
            self.current_index = min(self.current_index + 1, len(self.media_files) - 1)
        self.play_current()

    def play_previous(self):
        if self.is_looping:
            self.current_index = (self.current_index - 1) % len(self.media_files)
        else:
            self.current_index = max(self.current_index - 1, 0)
        self.play_current()

    def pause(self):
        self.is_paused = True

    def resume(self):
        self.is_paused = False
        self.play_current()

    def toggle_loop(self):
        self.is_looping = not self.is_looping
        print(f"Looping {'enabled' if self.is_looping else 'disabled'}")
