from auth.login import login 
from data.load_data import load_data 
from data.save_as_ics import save_as_ics
from mail_service.send_email import send_email

if __name__ == "__main__":
    

    username = input("请输入学号：>")
    password = input("请输入密码：>")

    # 登录获取session
    logined_session = login(username,password)

    # 获取课程数据
    data = load_data(logined_session)

    # 将数据保存为ICS文件
    save_as_ics(data)

    # 是否需要使用邮件发送
    is_send_email = input("是否需要使用邮件发送课程安排？(y/n):> ")
    if is_send_email.lower() == 'y':
        # 发送邮件
        send_email()
    else:
        print("课程安排已保存为courses.ics，邮件发送已跳过。")








