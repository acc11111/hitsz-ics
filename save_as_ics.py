from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz
import re
from ics.alarm import DisplayAlarm

def save_as_ics(data):
    calendar = Calendar()
    beijing_tz = pytz.timezone('Asia/Shanghai')
    for course in data:
        event = Event()
        event.name = course["BT"]
        # 使用正则表达式获取课的时间
        time_pattern = re.search(r'(\d{1,2}):(\d{2})-(\d{1,2}):(\d{2})', course["BT"])
        if time_pattern:
            start_hour = int(time_pattern.group(1))
            start_minute = int(time_pattern.group(2))
            end_hour = int(time_pattern.group(3))
            end_minute = int(time_pattern.group(4))
            
            event.begin = beijing_tz.localize(
            datetime.strptime(course["SJ"], "%Y-%m-%d") + 
            timedelta(hours=start_hour, minutes=start_minute)
            )
            event.duration = timedelta(
            hours=(end_hour - start_hour), 
            minutes=(end_minute - start_minute)
            )
        else:
            print(f"无法解析课程时间: {course['BT']}")
            continue
        event.location = "哈尔滨工业大学深圳校区" + course["NR"]
        calendar.events.add(event)
    with open('courses.ics', 'w', encoding='utf-8') as f:
        f.write(calendar.serialize())
        print("课程安排已保存为courses.ics")