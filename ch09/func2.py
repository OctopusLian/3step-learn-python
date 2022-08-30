'''
Author: neozhang
Date: 2022-08-30 15:50:17
LastEditors: neozhang
LastEditTime: 2022-08-30 15:53:20
Description: 请填写简介
'''
def get_triangle(base=1, height=1): # 设默认值
    return base * height / 2

area = get_triangle()
# area = get_triangle(height=6)
print('三角形的面积为', area, 'cm^2。') # 三角形的面积为 0.5 cm^2。
