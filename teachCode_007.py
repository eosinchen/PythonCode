# _*_ coding: utf-8 _*_

import time
from datetime import datetime
from threading import Timer
import random


# 依據 sleepSecond 的時間來執行與休眠
def timeWork(sleepSecond):

    for i in range(1, 21):
        print("第 " + str(i), end=" 次,  ")
        print("目前日期時間 => " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"), end=", ")
        print("溫度是 " + str(random.randint(10, 50)) + " 度")
        time.sleep(sleepSecond)

#
def printTime(inc):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    t = Timer(inc, printTime, (inc,))
    t.start()


# 主程式 -------------------------------------------------------------------------

# timeWork(2)
# printTime(5)