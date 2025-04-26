#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import base64
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user=input("请输入发送的邮箱:>")
mail_pass=input("请输入相应的授权码:>")  # 输入SMTP密码
 
 
sender = mail_user  # 发件人邮箱(最好写全, 不然会失败)
receivers = [input("请输入接收的邮箱:>")]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

 
# Create a multipart message
message = MIMEMultipart()
# Format the From header with a nickname
nickname = "测试发件人"
# Encode the Chinese nickname using base64
encoded_nickname = "=?utf-8?B?{}?=".format(base64.b64encode(nickname.encode('utf-8')).decode('utf-8'))
# Format the From field as "nickname <email>"
message['From'] = formataddr((encoded_nickname, sender))
# Similarly format the To header
message['To'] = formataddr(("测试收件人", receivers[0])) 

# Set the subject
subject = '课程安排'
message['Subject'] = Header(subject, 'utf-8')

# Add text body
message.attach(MIMEText('学期课程安排', 'plain', 'utf-8'))

# Attach the ICS file
ics_file = 'courses.ics'  # Change to your ICS filename
with open(ics_file, 'rb') as attachment:
    part = MIMEBase('text', 'calendar', method='REQUEST', name=os.path.basename(ics_file))
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment', 
                   filename=os.path.basename(ics_file))
    message.attach(part)
 
 
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 使用SSL连接，端口号465
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as e:
    print ("Error: 无法发送邮件")
    print(e)