import sys
import asyncio
import threading
from PyQt6 import QtWidgets
from Status import CustomStatus
from gui import WallpaperChangerGUI
from wallpaper import ImagePathLoader, WallPaperChanger
import qasync

def main():
    image_directory = 'D:\\MediaPlayerProject\\media'
    loader = ImagePathLoader(image_directory, 6)
    interval = 10  # Time interval in seconds
    changer = WallPaperChanger(interval)
    state = CustomStatus()

    def run_gui():
        app = QtWidgets.QApplication(sys.argv)

        # 使用 qasync 适配器来启动 asyncio 的事件循环
        loop = qasync.QEventLoop(app)
        asyncio.set_event_loop(loop)
        window = WallpaperChangerGUI(state, loader)

        # 使用 qasync 启动 Qt 和 asyncio 的事件循环
        with loop:
            loop.run_forever()

    # 在新线程中运行异步代码
    def run_async():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(changer.play_images(state, loader))

    threading.Thread(target=run_async).start()
    run_gui()

if __name__ == "__main__":
    main()
