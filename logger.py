from datetime import datetime

# 日志文件名称根据启动时间命名
log_filename = f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

def log_playing_file(file_path):
    with open("log/"+log_filename, 'a',encoding="UTF-8") as log_file:
        log_file.write(f"Playing: {file_path}\n")
    print(f"Logged: {file_path}")
