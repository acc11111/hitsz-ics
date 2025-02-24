import requests
from bs4 import BeautifulSoup
import sys

def login(username, password, code=None):
    session = requests.Session()
    default_request_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }
    session.headers.update(default_request_header)

    try:
        # 访问初始页面
        session.get("http://jw.hitsz.edu.cn/cas")

        # 请求登录页面
        response = session.get(
            "https://ids.hit.edu.cn/authserver/combinedLogin.do?type=IDSUnion&appId=ff2dfca3a2a2448e9026a8c6e38fa52b&success=http%3A%2F%2Fjw.hitsz.edu.cn%2FcasLogin"
        )
        doc1 = BeautifulSoup(response.text, 'html.parser')

        # 提取表单数据
        form = doc1.select_one("#authZForm")
        url = "https://sso.hitsz.edu.cn:7002" + form['action']
        client_id = doc1.select_one("input[name=client_id]")['value']
        scope = doc1.select_one("input[name=scope]")['value']
        state = doc1.select_one("input[name=state]")['value']

        # 准备提交的数据
        payload = {
            'action': 'authorize',
            'response_type': 'code',
            'redirect_uri': 'https://ids.hit.edu.cn/authserver/callback',
            'client_id': client_id,
            'scope': scope,
            'state': state,
            'username': username,
            'password': password
        }

        # 提交表单
        resp3 = session.post(url, data=payload)
        login = resp3.url.endswith("/authentication/main")
        cookies = session.cookies.get_dict()

        if not login:
            print("登录失败:", login)
            print("Cookies:", cookies)
            print("即将终止脚本，请重新运行！")
            sys.exit(1)

        else:
            print("登录成功:", login)
            print("Cookies:", cookies)

        return session
    
    except Exception as e:
        print("出现错误:", e)
    


if __name__ == '__main__':
    username = input("请输入学号>")
    password = input("请输入密码>")
    session = login(username, password)
    print(session)