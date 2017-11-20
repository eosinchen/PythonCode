# _*_ coding: utf-8 _*_

# if-elif-else 練習
# By Eosin Chen(eosinchen@gmail.com)

# if 判斷式基本型
# 算術運算符號 =(變數賦值), +, -, *, /, //(整除), **(次方), %(餘數), +(正數), -(負數)
# 關係運算符號 <, <=, ==(等於), !=, >, >=
def func_if():
    a = 300
    b = 200

    # if a > b: <= 判斷式上，加上括號比較好
    if (a > b):
        print("a 比 b 大")

# if-else 判斷式
def func_if_else():
    a = 100
    b = 200

    # else 後面不用接判斷式
    if (a > b):
        print("a 比 b 大")
    else:
        print("b 比 a 大")

# if-elif-else 判斷式
def func_if_elif_else():
    a = 200
    b = 200

    if (a > b):
        print("a 比 b 大")
    elif (a == b):
        print("a 和 b 相等")
    else:
        print("b 比 a 大")

# if 判斷式 - 多重條件
def func_if_multi_rule():
    a = 300
    b = 200
    c = 100

    # 邏輯運算符號 => and, or, not
    if (a > b) and (b > c):
        print("a 比 b 大，b 比 c 大")

# if 判斷式 - 巢狀
def func_if_nested():
    a = 300
    b = 200
    c = 100

    if (a > b):
        if (b > c):
            print("a 比 b 大，b 比 c 大")

# 主程式
func_if()

func_if_else()

func_if_elif_else()

func_if_multi_rule()

func_if_nested()