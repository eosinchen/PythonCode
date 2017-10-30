# 函數 練習
# By Eosin Chen(eosinchen@gmail.com)

# Python 函數語法
# def 函數名稱(傳入參數):
#     內縮敘述句
#     內縮敘述句
#     內縮敘述句
#     內縮敘述句
#     return n (用 return 結束函數，與傳回值)

# 用輾轉相除法求最大公約數
def gcd(m, n):
    if (n == 0):
        return m
    else:
        return gcd(n, m % n)




# 主程式
print(gcd(56, 16))

