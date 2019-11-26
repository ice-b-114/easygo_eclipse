# -*- coding: utf-8 -*-
import os
mp =r'D:/1/'
save_path = r'D:/3/'
flist = os.listdir(mp)#第一级目录，日期
sku = []
for f in flist:
    if "ed" in f:#判断是否带ed
        for f2 in os.listdir(os.path.join(mp,f)):#第二级目录，一次拍摄
            class_id = open(os.path.join(mp,f,f2, "class_id.txt"),"r+",encoding ="utf-8-sig")
            for line in class_id.readlines():#读取class_id文件
                sku.append(line)
sku = set(sku)
print(sku)
result = open(os.path.join(mp, "sku.txt"),"w+",encoding ="utf-8-sig")
for i in sku:
    result.write(i)
result.close()
print("完成")
