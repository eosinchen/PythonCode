# 函數 練習
# By Eosin Chen(eosinchen@gmail.com)

# Python 函數語法
# def 函數名稱(傳入參數):
#     內縮敘述句
#     內縮敘述句
#     內縮敘述句
#     內縮敘述句
#     return n (用 return 結束函數，與傳回值)

import time

# 用輾轉相除法求最大公約數
def gcd(m, n):
    if (n == 0):
        return m
    else:
        return gcd(n, m % n)

# Python 不支援 function overload
# 若有兩個以上相同名稱的 function
# 也不會出錯
# 但最後一個會覆蓋前者的定義

def sum(a, b):
    return a + b

#def sum(a, b, c):
#    return a + b + c

# 函數中，可以預設參數的值
# 即可用來解決參數個數不同的重載問題
def sum(a, b, c = 0):
    return a + b + c

# 函數和物件資源
def appendTo(element, arr = []):
    print("In Function => " ,end="")
    print(arr)
    arr.append(element)
    return arr

# 函數接受不定個數的參數
# 利用 * 將所有的參數，收集到一個 tuple(唯讀 List)中
def sum_many_item(*numbers):
    print(type(numbers))
    print(numbers)
    total = 0
    for number in numbers:
        total += number
    return total

# 函數接受不定個數的參數
# 型態不相同，名稱也有其意義
# 利用 * 將所有的參數，收集到一個 dict(key-value)中
# dict 格式 {"key1" : "value1", "key2" : 10, "key3" : "word1"}
def use_dict_argu(**dict):
    print(type(dict))
    print(dict)
    for dict_key in dict.keys():
        print(dict[dict_key])

# 巢狀函數
# 以選擇排序法為例
def selection(number):

    # def 中的 def
    # 找出未排序中最小值
    def min(m, j):
        if j == len(number):
            return m
        elif number[j] < number[m]:
            return min(j, j + 1)
        else:
            return min(m, j + 1)

    # 排序迴圈
    for i in range(0, len(number)):
        # 找出較小者
        m = min(i, i + 1)
        if i != m:
            # 進行交換
            number[i], number[m] = number[m], number[i]

# 遞迴呼叫
# 使用 費氏函數 為例
def fib_recursive(n):

    # 顯示時間
    print(time.strftime("%I:%M:%S"))

    # 遞迴呼叫的停止條件
    if (n == 0):
        return 0

    # 遞迴呼叫的停止條件
    if (n == 1):
        return 1

    # 顯示呼叫的結果
    sum_final = fib_recursive(n - 1) + fib_recursive(n - 2)
    print(sum_final)
    return sum_final

# 主程式 -------------------------------------------------------------------------
#print(gcd(56, 16))

# TypeError: sum() missing 1 required positional argument: 'c'
#print(sum(10, 20))

# 在呼叫函式時，並不一定要依參數宣告順序來傳入引數
# 可以指定參數名稱來設定其引數值，稱之為關鍵字引數
#print(sum(c = 50, a = 45, b = 63))

# 觀察以下的執行情況
#print(appendTo(10, [1, 2, 3]))

# 沒有傳入 arr 陣列時，會怎樣？
# 會建立一個 arr 物件
# 這個物件會一直都在
#print(appendTo(10))

#print(appendTo(20, [4, 5, 6]))

# 加到 appendto(10) 所建立的物件中
#print(appendTo(20))

# 加到 appendto(10) 所建立的物件中
#print(appendTo(30))

#print(appendTo(40))

#print(sum_many_item(10, 20))
#print(sum_many_item(10, 20, 30))
#print(sum_many_item(10, 20, 30, 100))

#use_dict_argu(ABC = 10, DFE = 20, DFG = "12345")

#number = [1, 5, 2, 3, 9, 7]
#selection(number)
#print(number)

#
print(fib_recursive(40))