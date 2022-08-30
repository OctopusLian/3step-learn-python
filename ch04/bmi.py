'''
Author: neozhang
Date: 2022-08-30 15:00:37
LastEditors: neozhang
LastEditTime: 2022-08-30 15:00:37
Description: 请填写简介
'''
weight = float(input('请输入体重（kg）：'))
height = float(input('请输入身高（m）：'))

bmi = weight / (height * height)
print('结果：', bmi)
