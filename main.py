import sys
import asyncio
from PyQt6 import QtWidgets
from Status import CustomStatus
from gui import WallpaperChangerGUI
from wallpaper import ImagePathLoader, WallPaperChanger
import qasync

def main():
    interval = 10  # Time interval in seconds
    seed=6
    image_directory = 'D:\\MediaPlayerProject\\media'
    loader = ImagePathLoader(image_directory, seed)
    changer = WallPaperChanger(interval)
    state = CustomStatus()

    # def run_gui():
    app = QtWidgets.QApplication(sys.argv)

    # 使用 qasync 适配器来启动 asyncio 的事件循环
    loop = qasync.QEventLoop(app)
    loop.create_task(changer.play_images(state, loader))
    asyncio.set_event_loop(loop)
    windows=WallpaperChangerGUI(state, loader) # 要防垃圾回收
    windows.show()

    # 使用 qasync 启动 Qt 和 asyncio 的事件循环
    with loop:
        loop.run_forever()


if __name__ == "__main__":
    main()
