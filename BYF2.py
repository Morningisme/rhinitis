#分析
import numpy as np
import time

p = r'C:\Users\Administrator\BY.txt'

with open(p,encoding = 'utf-8') as f:
    data = np.loadtxt(f,str,delimiter=",")
    Data = data.astype(np.int32)
    #相关性 内在联系 计算公式
    def Relevant(datas):
        tong = Data[:, 1]
        tongMean=np.mean(tong)
        datasMean =np.mean(datas)
        tongSTD =np.std(tong)
        datasSTD =np.std(datas)
        tongZ = (tong-tongMean)/tongSTD
        datasZ = (datas-datasMean)/datasSTD
        r = np.sum(tongZ*datasZ)/(len(tong))
        return r
    def F2(f2):
        f2 =' %.2f'%f2#保留2位浮点数
        return  f2
    tong = Data[:, 1]
    temperature = Data[:, 2]
    pepper = Data[:, 3]
    rest = Data[:, 4]
    snore = Data[:, 5]
    sport = Data[:, 6]
    face = Data[:, 7]
    work = Data[:, 8]
    emotion = Data[:, 9]
    music = Data[:, 10]
    lol = Data[:, 11]
    hair = Data[:, 12]
    shower = Data[:, 13]
    drug = Data[:, 14]


#输出 Relevant(datas)  范围在-1 ~ 1   1为正相关
    print('鼻炎与以下选项的相关性' + '\n')
    print('温度高不高?'+': '+str(F2(Relevant(temperature))))
    print('吃了多少辣椒以及刺激性食物?'+': '+str(F2(Relevant(pepper))))
    print('休息睡眠程度?' +': '+str(F2(Relevant(rest))))
    print('打呼噜程度?' +': '+str(F2(Relevant(snore))))
    print('锻炼程度?' +': '+str(F2(Relevant(sport))))
    print('按摩脸部酸痛处?' +': '+str(F2(Relevant(face))))
    print('工作压力和强度？' + ': '+str(F2(Relevant(work))))
    print('负面情绪？' +': '+str(F2(Relevant(emotion))))
    print('做了多少冥想、听了多少音乐？' +': '+str(F2(Relevant(music))))
    print('LOL程度？' +': '+str(F2(Relevant(lol))))
    print('绕头发多还是少？' +': '+str(F2(Relevant(hair))))
    print('洗澡泡热水脚？' +': '+str(F2(Relevant(shower))))
    print('中药、喷鼻药水？' +': '+str(F2(Relevant(drug))))