# -*- coding: utf-8 -*-
import re
def read_txt(txt_path):
    sku_dict = {}
    flag = 0
    with open(txt_path, "r+",encoding='utf-8-sig') as txt:
        for line in txt.readlines():
            line = line.strip('\n')#去掉换行符
            if flag == 0:
                matchobj = re.match(r'(.*)：(\d*)', line)
                sku = matchobj.group(1)
                num = matchobj.group(2)
                if sku in sku_dict:
                    pass
                else:
                    sku_dict.setdefault(sku, [num])
                flag = 1
            elif flag == 1:
                flag = 2
                continue
            elif line == "###":
                flag = 0
                continue
            elif flag == 2:
                sku_dict[sku].append(line)
    print("读入成功")
    return sku_dict            
dict1 = read_txt(r'D:/3/input.txt')
dict2 = read_txt(r'D:/3/input2.txt')
result_path = r'D:/3/combine.txt'

for sku in dict1.items():#sku = (sku,[num,目录...])
    if sku[0] in dict2:
        dict2[sku[0]][0] = int(dict2[sku[0]][0]) + int(sku[1][0])
        for i in sku[1][1:]:
            dict2[sku[0]].append(r'@'+i)
    else:
        dict2[sku[0]] = sku[1]
print(dict2)
with open(result_path, "w+",encoding='utf-8-sig') as sku_txt:
    for na,nu in dict2.items():
        sku = re.search(r'\d*', na).group()
        sku_txt.write(na+'：'+str(nu[0])+'\n')
        sku_txt.write("所在文件夹：\n")
        for j in nu[1:]:
            sku_txt.write(j+"\n")
        sku_txt.write("###\n")
print('合并完成')