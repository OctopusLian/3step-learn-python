'''
Author: neozhang
Date: 2022-08-30 15:07:11
LastEditors: neozhang
LastEditTime: 2022-08-30 15:19:39
Description: 请填写简介
'''
addresses = {
    '名无权兵卫': '千叶县千叶市美芳町1-1-1',
    '山田太郎': '东京都练马区藏王町2-2-2',
    '铃木花子': '埼玉县所泽市大竹町3-3-3',
}

print(addresses.pop('山田太郎')) # 东京都练马区藏王町2-2-2
print(addresses) # {'名无权兵卫': '千叶县千叶市美芳町1-1-1', '铃木花子': '埼玉县所泽市大竹町3-3-3'}
addresses.clear()
print(addresses) # {}
