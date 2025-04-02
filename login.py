import requests
from bs4 import BeautifulSoup
import sys
from encryptPassword import encrypt_password

def login(username, password):
    print("logging...")
    session = requests.Session()
    default_request_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    session.headers.update(default_request_header)

    try:
        # 访问初始页面

        ids_url = "https://ids.hit.edu.cn/authserver/login?service=http%3A%2F%2Fjw.hitsz.edu.cn%2FcasLogin"

        # 获取ids的登陆界面信息
        login_page = session.get(ids_url)
        soup = BeautifulSoup(login_page.text, 'html.parser')

        # 获取exection的值
        execution_element = soup.find('input', {'id': 'execution'})
        execution = execution_element['value'] if execution_element else None

        # 获取salt的值
        salt_element = soup.find('input', {'id': 'pwdEncryptSalt'})
        salt = salt_element['value'] if salt_element else None

        print(f"Execution: {execution}")
        print(f"Salt: {salt}")

        # 准备需要提交的登录数据
        login_data = {
            "username": username,
            "password": encrypt_password(password, salt),
            "captcha": "",
            "_eventId": "submit",
            "cllt": "userNameLogin",
            "dllt": "generalLogin",
            "lt": "",
            "execution": execution
        }

        # 发送登录请求
        login_response = session.post(ids_url, data=login_data)
        login = login_response.url.endswith("/authentication/main")

        if not login:
            print("登录失败:", login)
            print("即将终止脚本，请重新运行！")
            sys.exit(1)

        else:
            print("登录成功:", login)


        return session
    
    except Exception as e:
        print("出现错误:", e)
    


if __name__ == '__main__':
    username = input("请输入学号>")
    password = input("请输入密码>")
    session = login(username, password)
    print(session)