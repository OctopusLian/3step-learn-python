'''
Author: neozhang
Date: 2022-08-30 15:38:59
LastEditors: neozhang
LastEditTime: 2022-08-30 15:47:22
Description: 请填写简介
'''
import datetime 

file = open('hoge.txt', 'w', encoding='UTF-8')
file.write(str(datetime.datetime.now()) + '\n')
file.close()
print('文件已保存。')
