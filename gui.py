import tkinter as tk
from media_player import MediaPlayer

class MediaPlayerGUI:
    def __init__(self, root):
        self.root = root
        self.player = MediaPlayer()

        self.root.title("Media Player")
        
        # 允许窗口调整大小
        self.root.resizable(True, True)

        # 创建控制按钮
        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.play_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(pady=5)

        self.next_button = tk.Button(root, text="Next", command=self.next)
        self.next_button.pack(pady=5)

        self.prev_button = tk.Button(root, text="Previous", command=self.previous)
        self.prev_button.pack(pady=5)

        self.loop_button = tk.Button(root, text="Toggle Loop", command=self.toggle_loop)
        self.loop_button.pack(pady=5)

        # 可以设置窗口的初始大小
        self.root.geometry('300x200')

    def play(self):
        self.player.resume()

    def pause(self):
        self.player.pause()

    def next(self):
        self.player.play_next()

    def previous(self):
        self.player.play_previous()

    def toggle_loop(self):
        self.player.toggle_loop()

def start_gui():
    root = tk.Tk()
    gui = MediaPlayerGUI(root)
    root.mainloop()
