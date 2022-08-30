'''
Author: neozhang
Date: 2022-08-30 15:38:43
LastEditors: neozhang
LastEditTime: 2022-08-30 15:43:41
Description: 请填写简介
'''
import math

weight = float(input('请输入体重（kg）：'))
height = float(input('请输入身高（m）：'))

bmi = weight / (height * height)
print('结果：', math.floor(bmi)) # 去除小数点
