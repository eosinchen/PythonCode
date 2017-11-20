# _*_ coding: utf-8 _*_

# Firebase 與 Python 練習
# By Eosin Chen(eosinchen@gmail.com)

# 使用 post 和 get 來存取資料

# firebase package 要先安裝
# 使用: pip install firebase

# 在本程式中引入 firebase 套件
from firebase import firebase
import time

# 設定 Firebase DB 路徑，與相關物件
fbDbUrl = "https://firstpythonproject-3e702.firebaseio.com/"
fbDb = firebase.FirebaseApplication(fbDbUrl)

# Firebase 資料庫的格式為 JSON 物件
# 在 Python 中，則為 dict 物件
newData = [
    {'name': '王大'},
    {'name': '黃二'},
    {'name': '李三'},
    {'name': '趙四'},
]

# 將資料放到 FB 資料庫中
for data in newData:
    fbDb.post('/data', data)
    time.sleep(3)

# 自 FB 資料庫中，取出資料
getData = fbDb.get('/data', None)
for data in getData:
    print(getData[data]['name'])
