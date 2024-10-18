import asyncio

from PyQt6 import QtWidgets
from Status import CustomStatus
from wallpaper import ImagePathLoader, set_wallpaper


class WallpaperChangerGUI(QtWidgets.QWidget):
    def __init__(self, state: CustomStatus, loader: ImagePathLoader):
        super().__init__()
        self.prev_button = None
        self.pause_button = None
        self.next_button = None
        self.state = state
        self.loader = loader
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle('Wallpaper Changer')

        # 布局
        layout = QtWidgets.QVBoxLayout()

        # 暂停按钮
        self.pause_button = QtWidgets.QPushButton('Pause')
        self.pause_button.clicked.connect(self.toggle_pause)
        layout.addWidget(self.pause_button)

        # 上一张按钮
        self.prev_button = QtWidgets.QPushButton('Previous')
        self.prev_button.clicked.connect(self.previous_image)
        layout.addWidget(self.prev_button)

        # 下一张按钮
        self.next_button = QtWidgets.QPushButton('Next')
        self.next_button.clicked.connect(self.next_image)
        layout.addWidget(self.next_button)

        self.setLayout(layout)
        self.resize(300, 200)

    async def toggle_pause_async(self):
        if self.state.get_value() == "Resume":
            print("set to Pause")
            await self.state.set_value("Pause")
            self.pause_button.setText('Resume')
        else:
            print("set to Resume")
            await self.state.set_value("Resume")
            self.pause_button.setText('Pause')

    def toggle_pause(self):
        asyncio.create_task(self.toggle_pause_async())


    def previous_image(self):
        # 触发重置以进入下一次等待
        path = self.loader.previous_image_path()
        set_wallpaper(path)
        self.state.trigger_reset()

    def next_image(self):
        # 触发重置以进入下一次等待
        path = self.loader.next_image_path()
        set_wallpaper(path)
        self.state.trigger_reset()
