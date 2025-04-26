# HITSZ-ICS: 哈工大（深圳）课程表生成工具

## 简介

这是一个自动生成哈尔滨工业大学（深圳）课程表 ICS 文件的工具，可直接导入到各类日历应用中。

主要功能：

-   自动从官网获取课程信息并转换为标准 ICS 日历文件
-   支持自定义学期时间段
-   添加课程提前 15 分钟提醒功能
-   自动设置课程地点为哈工大深圳校区
-   支持通过邮件自动发送 ICS 文件

当前默认加载的是 2025 年秋季学期，时间范围可在 `load_data.py` 中修改：

```python
start_date = datetime(2025, 2, 24)
end_date = datetime(2025, 6, 22)
```

## 使用方法

### 1. 获取并运行项目

克隆仓库：

```bash
git clone https://github.com/acc11111/hitsz-ics.git
cd hitsz-ics
```

安装依赖：

```bash
pip install -r requirements.txt
```

生成 ICS 文件：

```bash
python main.py
```

### 2. 导入到日历应用

#### 自动邮件发送（推荐）

本项目支持使用邮箱账号以及 PASS 自动发送 ICS 文件

#### iPhone 导入方法

1. 在 iPhone 的邮件 APP 中绑定您的邮箱
2. 将生成的 `courses.ics` 文件通过邮件发送至该邮箱
3. 在 iPhone 上打开邮件，点击附件并选择"添加到日历"

#### 其他设备

-   Android: 下载 ICS 文件后导入 Google Calendar 或其他日历应用
-   电脑: 可直接导入到 Outlook、Google Calendar 等应用
