# -*- coding: utf-8 -*-
import os
import xml.etree.cElementTree as ET
from loguru import logger
logger.add("output.log", backtrace=True, diagnose=True)
def gci(filepath):
    files = os.listdir(filepath)
    for fi in files:
        fi_d = os.path.join(filepath,fi)
        if os.path.isdir(fi_d):
            gci(fi_d)
        elif 'xml' in fi:
            changee(fi_d)

def changee(xml):   
    global class_id
    root = ET.parse(xml)
    depth = root.find("size").find("depth").text
    assert depth == "3"
    for ob in root.findall("object"):
        name = ob.find("name").text + ob.find("skuName").text
        if name not in class_id:
            class_id.append(name)
            
if __name__=='__main__':
    try:
        xml_path = r"D:/meiyijia_1122/meiyijia_1122/"
        class_id = []
        with open(os.path.join(xml_path, "class_id.txt"), "w",encoding='utf-8-sig') as f:
            pass
        gci(xml_path)
        with open(os.path.join(xml_path, "class_id.txt"), "a+",encoding='utf-8-sig') as f:
            for id1 in class_id:
                f.write(id1+"\n")
        print(class_id)
    except:
        logger.exception('error')