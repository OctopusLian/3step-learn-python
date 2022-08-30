'''
Author: neozhang
Date: 2022-08-30 15:32:34
LastEditors: neozhang
LastEditTime: 2022-08-30 15:32:35
Description: 请填写简介
'''
point = int(input('你的成绩是？'))

if point >= 90:
    print('真棒！毫无疑问，你合格了！')
elif point >= 70:
    print('恭喜你，合格了！')
elif point >= 50:
    print('真遗憾，差一点就合格了。')
else:
    print('很遗憾，不合格。')
