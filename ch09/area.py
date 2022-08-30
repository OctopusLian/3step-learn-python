'''
Author: neozhang
Date: 2022-08-30 15:50:27
LastEditors: neozhang
LastEditTime: 2022-08-30 15:50:28
Description: 请填写简介
'''
import math

def get_circle(redius = 1):
    return redius * redius * math.pi
    
if __name__ == "__main__":
    print(get_circle(10), 'cm^2')
    print(get_circle(7), 'cm^2')
