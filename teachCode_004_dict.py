# _*_ coding: utf-8 _*_

# Dict 練習
# By Eosin Chen(eosinchen@gmail.com)

# dict 字典
# 由成對(key:vlue)的結構組成基本的鍵值
# 每一對鍵值，用 , 隔開，所有的鍵值組，放在大括號中

# 鍵值的限制
# 1. 鍵值可以是任何資料類型(字串、數字、布林)，但不可用變數
# 2. 若有重覆的鍵值，則後續的值，會覆蓋原先的值

# 建立一個 dict 變數(沒有初值)
dictVar1 = dict()

# 有初值的 dict 變數
# 其中鍵值必須為唯一，但值不必唯一
dictVar2 = {'name1':'王大', 'name2':'黃二', 'name3':'李三', 'name4':'趙四'}

# 鍵值可以是任何資料類型(字串、數字、布林)，只要是唯一即可，如下
dictVar3 = {'name':'王大', 1:'黃二', 2:'李三', True:'趙四'}

# 取得 dict 中的值
print(dictVar2['name1'])
print(dictVar2['name4'])

print(dictVar3['name'])
print(dictVar3[2])
print(dictVar3[True])

# 用迴圈取出 鍵值 與 值
for value in dictVar2:
    print(value)
    print(dictVar2[value])

# 修改某個值，直接指定即可
dictVar3[2] = "修改後"
print(dictVar3[2])

# 加入一項新的鍵值組合，直接給予新的 鍵值:值 即可
print(dictVar2)
dictVar2['name5'] = '張五'
print(dictVar2)

# 刪除一個鍵值，用 del 的命令
del dictVar2['name5']
print(dictVar2)

# 練習，試比較，以下三行命令，真正作用為何？
# 並寫下答案
# del dictVar2['name5']
# dictVar2.clear()
# del dictVar2

'''
其他功能
http://www.runoob.com/python/python-dictionary.html
 
排序方式
http://blog.yslin.tw/2012/05/python-listdict.html
'''

