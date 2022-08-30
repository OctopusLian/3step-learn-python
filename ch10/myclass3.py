'''
Author: neozhang
Date: 2022-08-30 16:25:23
LastEditors: neozhang
LastEditTime: 2022-08-30 16:31:31
Description: 请填写简介
'''
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        result = self.weight / (self.height * self.height)
        print(self.name, '的BMI为', result, '。')

# 继承Person类
class BusinessPerson(Person):
    def __init__(self, name, height, weight, title):
        super().__init__(name, height, weight)
        self.title = title

    def work(self):
        print(self.title, self.name, '正在工作。')
    