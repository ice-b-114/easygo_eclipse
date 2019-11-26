# -*- coding: utf-8 -*-
import xlrd
import os
import re
import shutil
excel_file = r'D:/保留sku.xls'
wb = xlrd.open_workbook(filename=excel_file)
sheet1 = wb.sheet_by_index(0)
#cols = tuple(sheet1.col_values(0))#读取excel
mp =r'D:/1/'
save_path = r'D:/3/'
flist = os.listdir(mp)#第一级目录，日期
for f in flist:
    if "ed" in f:#判断是否带ed
        for f2 in os.listdir(os.path.join(mp,f)):#第二级目录，一次拍摄
            flag = 0
            class_id = open(os.path.join(mp,f,f2, "class_id.txt"),"r+",encoding ="utf-8-sig")
            for line in class_id.readlines():#读取class_id文件
                #sku = re.search(r'\d*', line).group()
                if "方便" in line:
                    flag = 1
                    break
            if flag == 1:
                shutil.copytree(os.path.join(mp,f,f2), os.path.join(save_path,f2))
                print("已复制副本"+f2)
print("完成")
