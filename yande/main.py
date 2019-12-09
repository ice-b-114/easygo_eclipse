# -*- coding: UTF-8 -*-
import requests
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
#download_list = multiprocessing.Manager().dict()
def download(img_url,pname):
    global download_list
    sec = time.time()#计时
    r = requests.get(img_url,stream=True)
    pic_size = float(r.headers['content-length'])
    #print(r.status_code) # 返回状态码
    if r.status_code == 200:
        f = open(pname+'.jpg', 'wb')
        #显示文件下载进度
        count = 0
        timetemp = time.time()
        for chunk in r.iter_content(chunk_size = 512):
            if chunk:
                f.write(chunk)
                count += len(chunk)
                if time.time() - timetemp > 1:
                    p = count / pic_size * 100
                    print('{}:{:.2f}%'.format(pname,p))
                    #download_list[pname] = p
                    timetemp = time.time()
        f.close()
        sec = time.time() - sec
        res_text = "{} Done,{:.2f}s used".format(pname,sec)
    else:
        res_text = "{} Fail".format(pname)
    return res_text
def showdownloadlist():
    while True :
        time.sleep(2)
        print(str(download_list))
def main(limit,*tag):
    tags = '+'.join(tag)
    res=requests.get(url='http://yande.re/post.xml?limit='+str(limit)+'&tags='+tags)
    pic_address = re.findall(r'jpeg_url="(.*?)"', res.text, )
    pic_name = re.findall(r'<post id="(.*?)"', res.text, )
    pic_tag = re.findall(r'tags="(.*?)"', res.text, )
    pic_author = re.findall(r'source="(.*?)"', res.text, )
#    print(res.text)
    for i in range(0,limit):
        print('ID:'+pic_name[i])
        print('source:'+pic_author[i])
        print('tags:'+pic_tag[i])
        with open('info.txt', "a+",encoding='utf-8-sig') as f:
            f.write('ID:{}\nsource:{}\ntags:{}\n'.format(pic_name[i],pic_author[i],pic_tag[i]))
#多线程下载
    executor = ThreadPoolExecutor(max_workers=5)
    #all_task = [executor.submit(download,pic_address[i],pic_name[i]) for i in range(0,limit)]
    all_task = []
    #executor.submit(showdownloadlist())
    for i in range(0,limit):
        all_task.append(executor.submit(download,pic_address[i],pic_name[i]))
        print("{} Downloading...".format(pic_name[i]))
    for res in as_completed(all_task):
        print(res.result())
if __name__ == '__main__':
    main(2,"bottomless order%3Arandom")#order%3Arandom
    print("All downloading task done")