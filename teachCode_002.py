# _*_ coding: utf-8 _*_

# 迴圈(while & for) 練習
# By Eosin Chen(eosinchen@gmail.com)

import random

# while 基本型
def while_basic():
    random_count = random.randint(1, 6)
    print(random_count)

    # while random_count != 6: <= 判斷式上，加上括號比較好
    while (random_count != 6):
        random_count = random.randint(1, 6)
        print(random_count)

# 依照輸入的值來執行 while 次數
def while_input():
    while_count = 0  #用來記錄迴圈執行次數

    # 這兒有資料型態轉換 => int(...)
    input_count = int(input("請輸入迴圈執行次數："))
    print(input_count)

    while (while_count < input_count):
        while_count += 1 # while_count = while_count + 1
        print("目前執行到第 " + str(while_count) + " 次")

# ------------------------------------------------------------------------------
# for 迴圈 - 以 range 為範圍來執行
def for_range():

    # range(start, stop, step) <= start 到 stop-1, 以 step 為遞增值(若無內定為 1)
    for var in range(1, 6):
        print(var)

# for 迴圈 - 從資料結構中(變數)，取出值來執行
def for_string():
    myEngString = "My First String"
    myChnString = "我的中文字串"

    for char in myChnString:
        print(char)

# for 迴圈 - 從資料結構中(串列)，取出值來執行
def for_list():
    myList = [1, 3, 5, 7, 9, "A", "String"]

    for char in myList:
        print(char)

# for 迴圈 - 巢狀，九九乘法表
def for_nested():
    for i in range(2, 7, 4):
        for j in range(1, 10):

            # -----
            print("{}x{}={:>2}    ".format(i, j, i * j), end="")
            print("{}x{}={:>2}    ".format(i + 1, j, (i + 1) * j), end="")
            print("{}x{}={:>2}    ".format(i + 2, j, (i + 2) * j), end="")
            print("{}x{}={:>2}    ".format(i + 3, j, (i + 3) * j))
            #-----

            #-----
            #for k in range(i, i + 5):
            #    print("{}x{}={:>2}    ".format(k, j, k * j), end="")
            #print()
            #-----

        print()

# continue - for 迴圈 - 巢狀，九九乘法表
def for_nested_continue():
    for i in range(2, 9):
        if i != 2 and i != 6: continue
        for j in range(1, 10):
            for k in range(i, i + 5):
                print("{}x{}={:>2}    ".format(k, j, k * j), end="")
            print()
        print()

# break - while - random
def while_basic_break():
    while True:
        x = random.randint(1, 6)
        print(x)
        if x == 6: break

# 費氏函數 - loop 版
def fib_loop(n):

    # 用來存放最終值
    sum_final = 1
    # 用來存放前一個的值
    sum_prev_1 = 0
    # 數值移動時，暫存之用
    sum_temp = 0

    # 進行 n < 0, n == 0, n == 1 的處理
    if (n < 0):
        print("請輸入 0 以上的整數")
        return

    if (n == 0) or (n == 1):
        return n

    # 利用迴圈進行數值運算
    for i in range(2, n + 1):
        sum_temp = sum_final
        sum_final = sum_final + sum_prev_1
        sum_prev_1 = sum_temp
        # 顯示每一個階段的結果，以便除錯
        # 正式程式中，此行需移除
        print(str(i) + " => " +str(sum_final) + ", " + str(sum_prev_1) + ", " + str(sum_temp))

    return sum_final


# 主程式
#while_basic()

#while_input()

#for_range()

#for_string()

#for_list()

#for_nested()

#for_nested_continue()

#while_basic_break()

fib_loop(100)