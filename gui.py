import tkinter as tk
import os
from threading import Event

def create_gui(stop_event):
    window = tk.Tk()
    window.title("Wallpaper Slideshow")
    global pause_button
    pause_button = tk.Button(window, text="Pause", command=toggle_pause)
    pause_button.pack(pady=20)

    def on_close():
        stop_event.set()  # 设置事件，通知停止播放
        window.quit()  # 关闭窗口
        os._exit(0)  # 彻底终止整个程序

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()

pause_event = Event()
pause_event.set()  # Initially not paused

def toggle_pause():
    if pause_event.is_set():
        pause_event.clear()  # Pause
        pause_button.config(text="Resume")
    else:
        pause_event.set()  # Resume
        pause_button.config(text="Pause")
