#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File : Merge_data_set.py
# Author: LiuXuanhe
# Date : 2019/7/29
import os
import shutil
def main(mpath,mfolder):
    src_path = os.path.join(mpath, mfolder)
    des_path = os.path.join(mpath, mfolder)+r"_ed"
    folder_list = os.listdir(src_path)
    for folder in folder_list:
        if not os.path.exists(os.path.join(des_path, folder)):
            os.makedirs(os.path.join(des_path, folder, "jpg"))
        if not os.path.exists(os.path.join(des_path, folder, "jpg")):
            os.makedirs(os.path.join(des_path, folder, "jpg"))
        if not os.path.exists(os.path.join(des_path, folder, "xml")):
            os.makedirs(os.path.join(des_path, folder, "xml"))
        if not os.path.isfile(os.path.join(src_path, folder)):
            for file in os.listdir(os.path.join(src_path, folder)):
                if file[-4:] == ".jpg":
                    if os.path.exists(os.path.join(des_path, folder, "jpg/",file)):
                        print("有文件{}".format(os.path.join(des_path, folder, "jpg/", file)))
                        raise IOError
                    else:
                        shutil.copyfile(os.path.join(src_path, folder, file), os.path.join(des_path, folder, "jpg/", file))
                elif file[-4:] == ".xml":
                    if os.path.exists(os.path.join(des_path, folder, "xml/")+file):
                        print("有文件{}".format(os.path.join(des_path, folder, "xml/", file)))
                        raise IOError
                    else:
                        shutil.copyfile(os.path.join(src_path, folder, file), os.path.join(des_path, folder, "xml/", file))
        else:
            print("有文件{}".format(folder))
            raise IOError
            
if __name__ == '__main__':
    main(r"C:/Users\JSKJ\Desktop\1","20190601_1839")
    print("完成")