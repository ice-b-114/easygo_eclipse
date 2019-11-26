# -*- coding: utf-8 -*-
import os
import re
import xlrd
excel_file = r'D:/保留sku.xls'#XLS文件位置
wb = xlrd.open_workbook(filename=excel_file)
sheet1 = wb.sheet_by_index(0)
cols = tuple(sheet1.col_values(0))#读取excel

path = r'D:/3'#目标文件夹目录
mlist = os.listdir(path)
sku_dict = {}
for f in mlist:
    if os.path.isdir(os.path.join(path,f)):
        i = 0
        jpg_path = os.path.join(path,f,'jpg')
        jpg_list = os.listdir(jpg_path)
        for f1 in jpg_list:
            i += 1
        #os.rename(os.path.join(path,f), os.path.join(path,f)+'_'+str(i), src_dir_fd=None, dst_dir_fd=None)
        #print(f+"数量为："+str(i))
        class_id = open(os.path.join(path,f, "class_id.txt"),"r+",encoding ="utf-8-sig")
        for line in class_id.readlines():#读取class_id文件
            line = line.strip('\n')#去掉换行符
            if line in sku_dict:
                sku_dict[line][0] += i
            else:
                sku_dict.setdefault(line, [])
                sku_dict[line].append(i)
            sku_dict[line].append(f)
with open(os.path.join(path, "result.txt"), "w+",encoding='utf-8-sig') as sku_txt:
    for na,nu in sku_dict.items():
        sku = re.search(r'\d*', na).group()
        if sku in cols:
            sku_txt.write(na+'：'+str(nu[0])+'\n')
            sku_txt.write("所在文件夹：\n")
            for j in nu[1:]:
                sku_txt.write(j+"\n")
            sku_txt.write("###\n")
print("完成")