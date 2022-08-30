'''
Author: neozhang
Date: 2022-08-30 15:33:45
LastEditors: neozhang
LastEditTime: 2022-08-30 15:33:45
Description: 请填写简介
'''
ch = int(input('语文的成绩是？'))
ma = int(input('数学的成绩是？'))

if ch >= 70 and ma >= 70:
    print('合格了！')
elif ch >= 70 or ma >= 70:
    print('还差一点！攻克薄弱科目吧！')
else:
    print('很遗憾，不合格。')
