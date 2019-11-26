#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File : data.py
# Author: LiuXuanhe
# Date : 2019/7/29
import os
import cv2
import xml.etree.cElementTree as ET
def main(mpath,mfolder):
    '''
    save_path = r"C:/Users/JSKJ/Desktop/"+folder+r"_ed/jpg_cut"
    img_path = r"C:/Users/JSKJ/Desktop/"+folder+r"_ed/jpg"
    xml_path = r"C:/Users/JSKJ/Desktop/"+folder+r"_ed/xml"
    '''
    mfolder = mfolder+r"_ed/"
    save_path = r"C:/Users\JSKJ\Desktop\shenhe/jpg_cut"
    folder_list = os.listdir(os.path.join(mpath, mfolder))
    for folder in folder_list:
        if os.path.isdir(os.path.join(mpath,mfolder,folder)):
#             save_path = os.path.join(mpath, mfolder)+folder+r"/jpg_cut"
            img_path = os.path.join(mpath, mfolder)+folder+r"/jpg"
            xml_path = os.path.join(mpath, mfolder)+folder+r"/xml"
            xml_list = os.listdir(xml_path)
#             if not os.path.exists(save_path):
#                 os.makedirs(save_path)
            for xml_file in xml_list:
                root = ET.parse(os.path.join(xml_path, xml_file))
                img_name = os.path.join(img_path, root.find("filename").text)
                print(img_name)
                image = cv2.imread(img_name)
                print(image.shape)
                depth = root.find("size").find("depth").text
                assert depth == "3"
                i = 0
                for ob in root.findall("object"):
                    xmin = int(float(ob.find("bndbox").find("xmin").text))
                    ymin = int(float(ob.find("bndbox").find("ymin").text))
                    xmax = int(float(ob.find("bndbox").find("xmax").text))
                    ymax = int(float(ob.find("bndbox").find("ymax").text))
                    name = ob.find("name").text
                    # xmin,ymin
                    # xmax,ymax
            
                    cropImg = image[ymin:ymax, xmin:xmax]
                    save_path1 = os.path.join(save_path, name)
                    if not os.path.exists(save_path1):
                        os.makedirs(save_path1)
                    imagecutname = os.path.join(save_path1, root.find("filename").text+"_"+str(i)+".jpg")
                    i = i+1
                    print(imagecutname)
                    cv2.imwrite(imagecutname, cropImg)
        
        print("finish")

if __name__ == '__main__':
    main(r"D:/meiyijia_1122/meiyijia_1122/1/",'xiejia')#main(总文件夹所在的上级目录，总文件夹)