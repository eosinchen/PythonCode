# _*_ coding: utf-8 _*_
#
# 使用 matplotlib 來繪圖
#

import matplotlib.pyplot as pt
import numpy as np


def plot13_1():
    w = [1, 3, 4, 5, 9, 11]
    x = [1, 2, 3, 4, 5, 6]
    y = [20, 30, 14, 67, 42, 12]
    z = [12, 33, 43, 22, 34, 20]

    pt.plot(x, y, lw=2, label='Mary')
    pt.plot(w, z, lw=2, label='Tom')
    pt.xlabel('month')
    pt.ylabel('dollars (million)')
    pt.legend()
    pt.title('Program 13-1')
    pt.show()


def plot13_2():
    with open('popu.txt', 'r') as fp:
        populations = fp.readlines()

    city = list()
    popu = list()

    for p in populations:
        cc, pp = p.split(',')
        city.append(cc)
        popu.append(int(pp))

    ind = np.arange(len(city))

    pt.bar(ind, popu)
    pt.xticks(ind + 0.5, city)
    pt.title('Program 13-2')
    pt.show()

def plot13_3():
    with open('yrborn.txt', 'r') as fp:
        populations = fp.readlines()

    yrborn = dict()

    for p in populations:
        yr, tl, boy, girl = p.split()
        yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

    ind = np.arange(len(yrborn))
    yrlist = sorted(list(yrborn.keys()))
    bp = list()
    bp_b = list()
    bp_g = list()
    for yr in yrlist:
        boys = yrborn[yr]['boy']
        girls = yrborn[yr]['girl']
        bp.append(boys + girls)
        bp_b.append(boys)
        bp_g.append(girls)

    pt.subplot(211)
    pt.plot(bp)
    pt.xlim(0, len(bp) - 1)
    pt.title('1986 - 2015 (Total)')
    pt.subplot(212)
    pt.plot(bp_b)
    pt.plot(bp_g)
    pt.xlim(0, len(bp_b) - 1)
    pt.title('1986 - 2015 (Boy:Girl)')
    pt.show()


def plot13_4():
    with open('yrborn.txt', 'r') as fp:
        populations = fp.readlines()

    yrborn = dict()

    for p in populations:
        yr, tl, boy, girl = p.split()
        yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

    ind = np.arange(1986, 2016)
    yrlist = sorted(list(yrborn.keys()))
    bp = list()
    bp_b = list()
    bp_g = list()
    for yr in yrlist:
        boys = yrborn[yr]['boy']
        girls = yrborn[yr]['girl']
        bp.append(boys + girls)
        bp_b.append(boys)
        bp_g.append(girls)

    width = 0.35
    pt.subplot(211)
    pt.plot(ind, bp)
    pt.xlim(1986, 2015)
    pt.title('1986 - 2015 (Total)')

    pt.subplot(212)
    pt.bar(ind, bp_b, width, color='b')
    pt.bar(ind + 0.35, bp_g, width, color='r')
    pt.xlim(1986, 2015)
    pt.title('1986 - 2015 (Boy:Girl)')

    pt.show()


def plot13_5():

    def f1(x):
        return int(float(bp[x]) / float(school[x]))

    def f2(x):
        return float(float(school[x]) / float(bp[x]))

    with open('school.txt', 'r') as fp:
        schools = fp.readlines()

    school = list()
    for s in schools:
        school.append(int(s.split()[1]))

    with open('yrborn.txt', 'r') as fp:
        populations = fp.readlines()

    yrborn = dict()

    for p in populations:
        yr, tl, boy, girl = p.split()
        yrborn[yr] = {'boy': int(boy), 'girl': int(girl)}

    yrlist = sorted(list(yrborn.keys()))
    bp = list()
    for yr in yrlist:
        boys = yrborn[yr]['boy']
        girls = yrborn[yr]['girl']
        bp.append(boys + girls)
    yr = range(1986, 2016)
    ind = np.arange(len(bp))
    pt.subplot(221)
    pt.plot(yr, bp, lw=2)
    pt.xlim(1986, 2015)
    pt.title('1986 - 2015 (Total)')

    pt.subplot(222)
    pt.plot(yr, school, lw=2)
    pt.xlim(1986, 2015)
    pt.title('1986 - 2015 School Numbers')

    pt.subplot(223)
    pt.plot(yr, list(map(f1, ind)), lw=2)
    pt.xlim(1986, 2015)
    pt.title('Person/School')

    pt.subplot(224)
    pt.plot(yr, list(map(f2, ind)), lw=2, color='r')
    pt.xlim(1986, 2015)
    pt.title('School/Person')
    pt.show()


def plot13_6():
    degree = np.linspace(0, 2 * np.pi, 200)
    x = np.cos(degree)
    y = np.sin(degree)

    pt.xlim(-1.5, 1.5)
    pt.ylim(-1.5, 1.5)
    pt.plot(x, y, 'bo')
    pt.plot(0.5 * x, 1.5 * y, 'ro')

    pt.show()


def plot13_7():
    a = 1.5
    b = 1
    degree = np.linspace(0, 2 * np.pi, 200)
    x1 = a * (1 + np.cos(degree)) * np.cos(degree)
    y1 = a * (1 + np.cos(degree)) * np.sin(degree)

    x2 = a * np.sin(2 * degree)
    y2 = b * np.sin(degree)

    pt.xlim(-2, 3.5)
    pt.ylim(-2.5, 2.5)
    pt.plot(x1, y1, color='red', lw=2)
    pt.plot(x2, y2, color='blue', lw=2)
    pt.savefig('mypic.png', format='png', dpi=200)
    pt.show()

# 主程式 -------------------------------------------------------------------------

# plot13_1()
# plot13_2()
# plot13_3()
# plot13_4()
# plot13_5()
# plot13_6()
plot13_7()