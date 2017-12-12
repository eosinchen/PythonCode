# _*_ coding: utf-8 _*_

# import time 作為時間的基本處理套件
import time
from datetime import datetime
from datetime import timedelta


# 日期和時間的時間戳(1970 - 2038 年)
def gettime():
    timestamp = time.time()
    print(timestamp)


# 轉換成本地時間
def getlocaltime():
    localtime = time.localtime(time.time())
    print(localtime)


# 將時間格式化
def getformattime():
    formattime = time.asctime(time.localtime(time.time()))
    print(formattime)

'''
%a 星期幾的簡寫
%A 星期幾的全稱
%b 月分的簡寫
%B 月份的全稱
%c 標準的日期的時間串
%C 年份的後兩位數字
%d 十進製表示的每月的第幾天
%D 月/天/年
%e 在兩字元域中，十進製表示的每月的第幾天
%F 年-月-日
%g 年份的後兩位數字，使用基於周的年
%G 年分，使用基於周的年
%h 簡寫的月份名
%H 24小時制的小時
%I 12小時制的小時
%j 十進製表示的每年的第幾天
%m 十進製表示的月份
%M 十時製表示的分鐘數
%n 新行符
%p 本地的AM或PM的等價顯示
%r 12小時的時間
%R 顯示小時和分鐘：hh:mm
%S 十進制的秒數
%t 水平製表符
%T 顯示時分秒：hh:mm:ss
%u 每周的第幾天，星期一為第一天 （值從0到6，星期一為0）
%U 第年的第幾周，把星期日做為第一天（值從0到53）
%V 每年的第幾周，使用基於周的年
%w 十進製表示的星期幾（值從0到6，星期天為0）
%W 每年的第幾周，把星期一做為第一天（值從0到53）
%x 標準的日期串
%X 標準的時間串
%y 不帶世紀的十進制年份（值從0到99）
%Y 帶世紀部分的十制年份
%z，%Z 時區名稱，如果不能得到時區名稱則返回空字元。
%% 百分號
'''

# 自訂日期呈現方式(自訂格式化)
def getstrftime():
    strftime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(strftime)

# 將日期字串轉換為時間戳
def converttotime():
    strtime = "2017-12-12 10:10:35"
    strstime = time.mktime(time.strptime(strtime, "%Y-%m-%d %H:%M:%S"))
    print(strstime)


# 日期時間的計算
# 利用 datetime 套件來幫助運算
# 日期運算 (1)計算之前/之後的日期 (2)計算相隔時間差
def getnexttime():
    now = datetime.now()
    aDay = timedelta(days=1)
    now = now + aDay
    print(now.strftime('%Y-%m-%d'))


# 計算時間差
def gettimediff():
    d1 = datetime.now()
    time.sleep(10)
    eclipseTimes = datetime.now() - d1
    print(eclipseTimes.total_seconds())


# 主程式 -------------------------------------------------------------------------

gettime()
getlocaltime()
getformattime()
getstrftime()
converttotime()
getnexttime()
gettimediff()

