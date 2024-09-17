from threading import Thread, Event
from gui import create_gui
from wallpaper import play_images
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
        # 创建一个 Event 来控制图片播放终止
        stop_event = Event()

        # 启动 GUI 线程，并传入 stop_event
        gui_thread = Thread(target=create_gui, args=(stop_event,))
        gui_thread.start()

        # 启动图片播放线程，并传入 stop_event
        play_thread = Thread(target=play_images, args=(images, log_filename, interval, stop_event))
        play_thread.start()

if __name__ == "__main__":
    main()
