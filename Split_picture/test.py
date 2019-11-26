# -*- coding: utf-8 -*-
import os 
import re
main_path = r'D:/meiyijia_1122\meiyijia_1122'
with open(os.path.join(main_path, "class_id.txt"), "r",encoding='utf-8-sig') as id_f:
    with open(os.path.join(main_path, "sku.txt"), "r",encoding='utf-8-sig') as sku_f:
        sku = []
#         for line in sku_f.readlines():
#             line = line.strip('\n')
#             sku.append(line)
        for line in id_f.readlines():
            line = line.strip('\n')
            cid = re.search(r'\d*', line).group()
            if cid in sku:
                print(line)
            sku.append(cid)