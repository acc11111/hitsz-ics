# 简介
通过使用官网的日程获取课程信息并转换为ics文件
目前加载的时间是2025秋季学期，可以在load_data.py内修改，相关的代码如下：
```
start_date = datetime(2025, 2, 24)
end_date = datetime(2025, 6, 22)
```
同时添加了提前15分钟提醒功能后会出现
```bash
 FutureWarning: Behaviour of str(Component) will change in version 0.9 to only return a short description, NOT the ics representation. Use the explicit Component.serialize() to get the ics representation.
  warnings.warn(
```
但是问题不大，还是可以正常使用
# 使用
### 获取ics文件
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
### 加载至iPhone
>网络上有很多教程的，比较方便的是发送邮件

S1：iPhone的邮件APP绑定邮箱A

S2：电脑上使用邮箱B发送生成的附件courses.ics至邮箱B

S3：iPhone打开邮箱APP点开附件的ics添加入日历即可



