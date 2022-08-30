'''
Author: neozhang
Date: 2022-08-30 15:33:32
LastEditors: neozhang
LastEditTime: 2022-08-30 15:33:32
Description: 请填写简介
'''
point = int(input('你的成绩是？'))

if point >= 70:
    print('合格了！')
else:
    print('很遗憾，不合格。')
    if point >= 50:
        print('但是就差一点了！')
    else:
        print('更加努力吧！')
