import requests
from bs4 import BeautifulSoup
import sys
import base64
import random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_password(password, salt):
    """使用盐值加密密码"""
    try:
        # AES加密字符集（与JavaScript匹配）
        AES_CHARS = "ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
        
        # 生成指定长度的随机字符串
        def random_string(length):
            return ''.join(random.choice(AES_CHARS) for _ in range(length))
        
        # 使用AES-CBC和PKCS7填充加密数据
        def get_aes_string(data, key, iv):
            data = data.encode('utf-8')
            key = key.encode('utf-8')[:16]  # 确保密钥为16字节
            iv = iv.encode('utf-8')[:16]    # 确保IV为16字节
            cipher = AES.new(key, AES.MODE_CBC, iv)
            padded_data = pad(data, AES.block_size)
            encrypted = cipher.encrypt(padded_data)
            return base64.b64encode(encrypted).decode('utf-8')
        
        # 如果没有盐值，直接返回原始密码
        if not salt:
            return password
            
        # 使用64字符前缀和16字符IV进行加密
        prefix = random_string(64)
        iv = random_string(16)
        return get_aes_string(prefix + password, salt, iv)
    except:
        return password


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
    

# 测试
if __name__ == '__main__':
    username = input("请输入学号>")
    password = input("请输入密码>")
    session = login(username, password)
    print(session)