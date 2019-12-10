# -*- coding: utf-8 -*-
'''
import time
from concurrent.futures import ThreadPoolExecutor
class download_list:
    download_list = dict()
    @classmethod
    def show(cls):
        while True:
            time.sleep(1)
            print(str(cls.download_list))
    @classmethod
    def show2(cls):
        for i,j in cls.download_list.item():
            print('{}:{:.2f}%'.format(i,j),end='')
            print('')
    @classmethod
    def set(cls,pname,precent):
        cls.download_list[pname] = precent

def change():
    time.sleep(4)
    download_list.set(1919, 8)
    time.sleep(4)
    download_list.set(1919, 100)
    download_list.set(114514,100)
executor = ThreadPoolExecutor(max_workers=5)
executor.submit(download_list.show)
executor.submit(change)
download_list.set(114514, 98)
time.sleep(10)
download_list.show2()
'''
import time
for i in range(10):
    print("\r离程序退出还剩%s秒" % (9-i), end="")
    time.sleep(1)