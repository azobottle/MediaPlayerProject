import tkinter as tk
import os
from threading import Event

pause_event = Event()
pause_event.set()  # Initially not paused

def create_gui(stop_event, images, current_index, change_image_callback):
    window = tk.Tk()
    window.title("Wallpaper Slideshow")

    # 定义 pause_button 为局部变量，并在函数中访问
    def toggle_pause():
        if pause_event.is_set():
            pause_event.clear()  # Pause
            pause_button.config(text="Resume")
        else:
            pause_event.set()  # Resume
            pause_button.config(text="Pause")

    def on_close():
        stop_event.set()  # 设置事件，通知停止播放
        window.quit()  # 关闭窗口
        os._exit(0)  # 彻底终止整个程序

    def show_next_image():
        current_index[0] = (current_index[0] + 1) % len(images)  # 下一张图片
        change_image_callback(current_index[0])

    def show_prev_image():
        current_index[0] = (current_index[0] - 1) % len(images)  # 上一张图片
        change_image_callback(current_index[0])

    # 将 pause_button 定义在 create_gui 函数作用域内
    pause_button = tk.Button(window, text="Pause", command=toggle_pause)
    pause_button.pack(pady=20)

    prev_button = tk.Button(window, text="Previous", command=show_prev_image)
    prev_button.pack(pady=10)

    next_button = tk.Button(window, text="Next", command=show_next_image)
    next_button.pack(pady=10)

    window.protocol("WM_DELETE_WINDOW", on_close)
    window.mainloop()
