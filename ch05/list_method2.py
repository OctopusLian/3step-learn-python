'''
Author: neozhang
Date: 2022-08-30 15:07:04
LastEditors: neozhang
LastEditTime: 2022-08-30 15:12:20
Description: 请填写简介
'''
names = ['山田太郎', '佐藤次郎', '铃木花子', '井上健太', '小川裕子']

print(names.pop(3))  # 井上健太
names.remove('小川裕子')
print(names) # ['山田太郎', '佐藤次郎', '铃木花子']
