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

    print(f"从{date_list[0]}到{date_list[-1]}一共获取了{len(date_list)}天的数据")

    data = []
    for date in date_list:
        formdata = {
            "rcrq": date,
        }
        response = session.post(query_url, data=formdata)
        data.extend(response.json())
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    return data