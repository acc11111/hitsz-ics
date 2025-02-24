from login import login 
from load_data import load_data 
import json
from ics import Calendar, Event
from datetime import datetime, timedelta
import pytz
import re


username = input("请输入学号：>")
password = input("请输入密码：>")

logined_session = login(username,password)

# 获取课程数据
data = load_data(logined_session)

# 读取节次时间映射
time_map = json.load(open('section_time_mappings.json', encoding='utf-8'))

# 转换为ics
def convert_to_ics(data):
    calendar = Calendar()
    beijing_tz = pytz.timezone('Asia/Shanghai')
    for course in data:
        event = Event()
        event.name = re.sub(r'(?<!^:)[^\u4e00-\u9fa5:]', '', course["BT"]).rstrip(':')
        for item in time_map:
            if item["节次"] == course["KSJC"]:
                event.begin = beijing_tz.localize(datetime.strptime(course["SJ"], "%Y-%m-%d") + timedelta(hours=datetime.strptime(item["开始时间"], "%H:%M").time().hour, minutes=datetime.strptime(item["开始时间"], "%H:%M").time().minute))
        event.duration = timedelta(hours=1, minutes=45)  # Assuming each course lasts 1 hour and 45 minutes
        event.location = course["NR"]
        calendar.events.add(event)
    # print(calendar)
    with open('courses.ics', 'w', encoding='utf-8') as f:
        f.writelines(calendar)

convert_to_ics(data)



