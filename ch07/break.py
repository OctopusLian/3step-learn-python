'''
Author: neozhang
Date: 2022-08-30 15:35:38
LastEditors: neozhang
LastEditTime: 2022-08-30 15:35:38
Description: 请填写简介
'''
colors = ['黑', '白', '×', '蓝', '绿']
# colors = ['黑', '白', '红', '蓝', '绿']

for color in colors:
    if color == '×':
        break
    print(color)
else:
    print('处理结束。')
