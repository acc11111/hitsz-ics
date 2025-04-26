from datetime import datetime, timedelta
import json

def load_data(session):
    query_url = "http://jw.hitsz.edu.cn/component/queryrcxxlist"
    start_date = datetime(2025, 2, 24)
    end_date = datetime(2025, 6, 22)
    date_list = []

    current_date = start_date
    while current_date <= end_date:
        date_list.append(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)

    print(f"准备从{date_list[0]}到{date_list[-1]}获取{len(date_list)}天的数据")
    print("如果需要修改获取数据的日期范围，请修改load_data.py中的start_date和end_date")
    print("正在获取数据，请稍等...")

    data = []
    for date in date_list:
        formdata = {
            "rcrq": date,
        }
        response = session.post(query_url, data=formdata)
        data.extend(response.json())
    # with open('data.json', 'w') as json_file:
    #     json.dump(data, json_file, ensure_ascii=False, indent=4)
    print("数据获取完成")
    return data