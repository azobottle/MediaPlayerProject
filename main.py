from threading import Thread, Event
from gui import create_gui
from wallpaper import play_images, change_image
from utils import get_images_from_directory
from datetime import datetime
import random

def main():
    image_directory = 'D:\\MediaPlayerProject\\media'
    interval = 10  # Time interval in seconds

    images = get_images_from_directory(image_directory)
    random.shuffle(images)
    log_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

    if not images:
        print("No images found in the directory.")
    else:
        stop_event = Event()

        # 初始化 current_index 为全局变量
        current_index = [0]  # 用列表以便传引用

        # 启动 GUI 线程，并传入 stop_event、图片列表和共享的 current_index
        gui_thread = Thread(target=create_gui, args=(stop_event, images, current_index, lambda idx: change_image(idx, images)))
        gui_thread.start()

        # 启动图片播放线程，并传入 stop_event 和共享的 current_index
        play_thread = Thread(target=play_images, args=(images, log_filename, interval, stop_event, current_index))
        play_thread.start()

if __name__ == "__main__":
    main()
