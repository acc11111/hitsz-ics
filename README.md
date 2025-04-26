# 简介

通过使用官网的日程获取课程信息并转换为 ics 文件
目前加载的时间是 2025 秋季学期，可以在 load_data.py 内修改，相关的代码如下：

```
start_date = datetime(2025, 2, 24)
end_date = datetime(2025, 6, 22)
```

同时添加了提前 15 分钟提醒功能后会出现
添加了锁定地址为哈尔滨工业大学深圳校区

```bash
 FutureWarning: Behaviour of str(Component) will change in version 0.9 to only return a short description, NOT the ics representation. Use the explicit Component.serialize() to get the ics representation.
  warnings.warn(
```

但是问题不大，还是可以正常使用

# 使用

### 获取 ics 文件

GET IT！

```bash
git clone https://github.com/acc11111/hitsz-ics.git
```

```bash
cd hitsz-ics
```

配置环境

```bash
pip install -r requirements.txt
```

GOGOGO!

```
python main.py
```

### 加载至 iPhone

目前本项目已经支持使用 email 的 pass 来实现自动发送

> 网络上有很多教程的，比较方便的是发送邮件

S1：iPhone 的邮件 APP 绑定邮箱 A

S2：电脑上使用邮箱 B 发送生成的附件 courses.ics 至邮箱 B

S3：iPhone 打开邮箱 APP 点开附件的 ics 添加入日历即可
