# _*_ coding: utf-8 _*_

# Set 練習
# By Eosin Chen(eosinchen@gmail.com)

# set 集合
# 為 無序、不重覆 的資料集合
# 可用來消除重覆資料
# 並可運行一些數學運算，如 交集、聯集、差集 等

# 建立一個 set 變數(沒有初值)
setVar1 = set()

# 有初值的 set 變數，用大括號做集合的表示
# 請注意，'A' 只會留下一個
# 數字、字串、布林，皆可當 set 的元素
setVar2 = {'A', 'B', 'C', 'D', 'A','XYZ', 123, 12345, 456, True, False}

# 亦可用 set 函數，將字串內容拆開
setVar3 = set('ABCDABEF')

# 觀察 set 類型的值
print(setVar1)
print(setVar2)
print(setVar3)

# 取得 set 的長度 - len
print(len(setVar1))
print(len(setVar2))
print(len(setVar3))

# 用迴圈取出 set 的內容
for value in setVar2:
    print(value)

# 用 add 加入某個值
setVar3.add('PQRST')
print(setVar3)

# 用 remove 移除某個值
setVar3.remove('A')
print(setVar3)

# pop 會任意移除一個值(這是無法預知的)
setVar3.pop()
print(setVar3)

# 集合和集合之間，進行運算
#
# 交集 => &
# 聯集 => |
# 差集 => -
# 等於 => ==
# 不等於 => !=
# 在...之中 => in
# 不在...之中 => not in
#

setVar4 = {'A', 'B', 'C'}
setVar5 = {'A', 'B', 'D', 'E', 'F'}

# 交集 => &
print(setVar4 & setVar5)

# 聯集 => |
print(setVar4 | setVar5)

# 差集 => -
print(setVar4 - setVar5)
print(setVar5 - setVar4)

# 在...之中 => in
if 'A' in setVar5:
    print('A 在 setVar5 之中')
