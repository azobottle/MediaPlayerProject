import os

def get_images_from_directory(directory, extensions=['.jpg', '.png', '.bmp']):
    image_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                image_files.append(os.path.join(root, file))
    return image_files

def getWeekRange():
    from datetime import datetime, timedelta
    # 获取当前日期
    current_date = datetime.now()

    # 计算当前日期是星期几（0=星期一，6=星期日）
    day_of_week = current_date.weekday()

    # 计算当前星期的开始日期（星期一）
    start_of_week = current_date - timedelta(days=day_of_week)

    # 计算当前星期的结束日期（星期日）
    end_of_week = start_of_week + timedelta(days=6)

    # 格式化日期
    start_of_week_str = start_of_week.strftime('%Y-%m-%d')
    end_of_week_str = end_of_week.strftime('%Y-%m-%d')

    # 生成星期的日期范围字符串
    week_range_str = f"{start_of_week_str} to {end_of_week_str}"
    return week_range_str