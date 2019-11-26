#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File : data.py
# Author: LiuXuanhe
# Date : 2019/7/29
import os
import xml.etree.cElementTree as ET
def main(mpath,mfolder):
    folder_list = os.listdir(os.path.join(mpath, mfolder)+r"_ed")
    for folder in folder_list:
        flag = "train"
        base_path = os.path.join(mpath, mfolder)+r"_ed/"+folder
        img_path = os.path.join(mpath, mfolder)+r"_ed/"+folder+r"/jpg"
        xml_path = os.path.join(mpath, mfolder)+r"_ed/"+folder+r"/xml"
        label_txt = "label.txt"
        xml_list = os.listdir(xml_path)
        class_id = []
        if flag == "test":
            with open(os.path.join(base_path, "class_id.txt"), "r") as f:
                class_id.append(f.read())
            class_id = [id.split("\n") for id in class_id][0]
        with open(os.path.join(base_path, label_txt), "w") as f:
            pass
        with open(os.path.join(base_path, "class_id.txt"), "w") as f:
            pass
        for xml_file in xml_list:
            root = ET.parse(os.path.join(xml_path, xml_file))
            img_name = root.find("filename").text
            depth = root.find("size").find("depth").text
            assert depth == "3"
            with open(os.path.join(base_path, label_txt), "a+") as f:
                f.write(img_name)
            for ob in root.findall("object"):
                xmin = int(float(ob.find("bndbox").find("xmin").text))
                ymin = int(float(ob.find("bndbox").find("ymin").text))
                xmax = int(float(ob.find("bndbox").find("xmax").text))
                ymax = int(float(ob.find("bndbox").find("ymax").text))
                name = ob.find("name").text + ob.find("skuName").text
                if name == "751249241128" or name == "751249252261" or name == "751249252452" or name == "751249130101" or name == "751249111346" or name == "751249130309":
                    name = "751249241128"
                if name == "5741000138847" or name == "5741000138878" or name == "5741000138908":
                    name = "5741000138908"
                if name == "6948960100108" or name == "5014379002836":
                    name = "5014379002836"
                if name == "9999999999999":
                    pass
                else:
                    if name not in class_id:
                        class_id.append(name)
                    index = class_id.index(name)
                    with open(os.path.join(base_path, label_txt), "a+") as f:
                        f.write(" " + ",".join([str(xmin), str(ymin), str(xmax), str(ymax), str(index)]))
            with open(os.path.join(base_path, label_txt), "a+") as f:
                f.write("\n")
        if flag == "train":
            with open(os.path.join(base_path, "class_id.txt"), "a+",encoding='utf-8-sig') as f:
                for id1 in class_id:
                    f.write(id1+"\n")
        print(class_id)

if __name__ == '__main__':
    main(r"C:/Users\JSKJ\Desktop\1","20190601_1839")