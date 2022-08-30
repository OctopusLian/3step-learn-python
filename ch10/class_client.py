'''
Author: neozhang
Date: 2022-08-30 15:59:44
LastEditors: neozhang
LastEditTime: 2022-08-30 16:16:09
Description: 请填写简介
'''
import myclass

# p1 = myclass.Person()
# print(p1)

p1 = myclass.Person('张三', 1.21, 23)
bmi1 = p1.weight / (p1.height * p1.height)
print(p1.name, '的BMI为', bmi1, '。') # 张三 的BMI为 15.709309473396626 。

p2 = myclass.Person('李四', 1.35, 30)
bmi2 = p2.weight / (p2.height * p2.height)
print(p2.name, '的BMI为', bmi2, '。') # 李四 的BMI为 16.46090534979424 。
