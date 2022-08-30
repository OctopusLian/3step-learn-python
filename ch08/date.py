'''
Author: neozhang
Date: 2022-08-30 15:38:52
LastEditors: neozhang
LastEditTime: 2022-08-30 15:44:52
Description: 请填写简介
'''
import datetime

today = datetime.date.today()
print('今天是', today, '。')  # 今天是 2022-08-30
birth = datetime.date(today.year, 6, 25)
ellap = birth - today
if ellap.days == 0:
    print('今天过生日！')
elif ellap.days > 0:
    print('距离今年的生日还有', ellap.days, '天。')
else:
    print('今年的生日已经过去', -ellap.days, '天了。')  # 今年的生日已经过去 66 天了。
