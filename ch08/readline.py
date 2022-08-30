'''
Author: neozhang
Date: 2022-08-30 15:39:07
LastEditors: neozhang
LastEditTime: 2022-08-30 15:48:11
Description: 请填写简介
'''
file = open('sample.txt', 'r', encoding='UTF-8')
data = file.readlines()
for line in data:
    print(line, end='')
file.close()
