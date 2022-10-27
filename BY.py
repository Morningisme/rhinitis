#000鼻炎困扰，通过记录每天可能导致鼻炎的因素与鼻塞程度，分析最佳限制鼻塞的方案
#创建CSV文件
# 1打开文件读取并分析历史数据相关性 2输入新的数据并保存


import numpy as np

import time
#高10低1
timeing=time.strftime('%Y%m%d')#1
print("今天是：" + str(timeing))

tong=input("鼻子通不通?")#2
temperature=input('温度高不高?')#3
pepper=input('吃了多少辣椒以及刺激性食物?')#4
rest=input('休息睡眠程度?')#5
snore=input('打呼噜程度?')#6
sport=input('锻炼程度?')#7
face=input('按摩脸部酸痛处?')#8
work=input('工作压力和强度？')#9
emotion=input('负面情绪？')#10
music=input('做了多少冥想、听了多少音乐？')#11
lol=input('LOL程度？')#12 一次9 两次10 自动 5 没有 1 看听3
hair=input('绕头发多还是少？')#13
shower = input('洗澡泡热水脚？')#14
drug = input('中药、喷鼻药水？')#15


PATH = r'C:\Users\Administrator\BY.txt'
F = open(PATH, "a+", encoding='utf-8')
F.write(timeing + ',' \
        + tong + ',' \
        + temperature +',' \
        + pepper +',' \
        + rest +',' \
        + snore +',' \
        + sport +',' \
        + face +',' \
        + work +',' \
        + emotion +',' \
        + music +',' \
        + lol +',' \
        + hair +',' \
        + shower +',' \
        + drug +'\n')

F.close()
