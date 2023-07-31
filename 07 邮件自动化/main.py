# 中国国内现在注册不了google
# https://learnku.com/python/t/47406

import os
import pandas as pd
import openpyxl
import yagmail
import datetime
import time

from news import NewsFeed

absolute_path = os.path.abspath('.') + '/files'


def send_email():
    # 读取xlsx文件
    df = pd.read_excel(f'{absolute_path}/data.xlsx')

    imap = 'scrjruzummymjeci'
    mail_server = "smtp.qq.com"
    email = yagmail.SMTP(user='1245924849@qq.com', password=imap, host=mail_server)
    for index, row in df.iterrows():
        now = datetime.datetime.now().strftime("%Y-%m-%d")
        yesterday = (datetime.datetime.now() - datetime.timedelta(days=15)).strftime("%Y-%m-%d")
        news_feed = NewsFeed(row["interest"], yesterday, now)
        email.send(to=f'{row["email"]}', subject='发送邮件测试', contents=f'你好啊 {row["name"]}!\n  '
                                                                          f'下面是关于你感兴趣的{row["interest"]} \n'
                                                                          f'内容如下：{news_feed.get()}', )
    print('发送成功!')


while True:
    if datetime.datetime.now().hour == 14 and datetime.datetime.now().minute == 19:
        send_email()
        time.sleep(60)
