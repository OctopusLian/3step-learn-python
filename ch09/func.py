'''
Author: neozhang
Date: 2022-08-30 15:49:21
LastEditors: neozhang
LastEditTime: 2022-08-30 15:51:37
Description: 请填写简介
'''
def get_triangle(base, height):
    return base + height / 2

area = get_triangle(10, 5)
print('三角形的面积为', area, 'cm^2。') # 三角形的面积为 12.5 cm^2。
