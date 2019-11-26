#coding=utf-8

import os

files = os.listdir('.')
#print('files',files)
for filename in files:
	portion = os.path.splitext(filename)
	# 如果后缀是.dat
	if portion[1] == ".jpeg":
		# 重新组合文件名和后缀名
		newname = portion[0] + ".jpg"   
		os.rename(filename,newname)
