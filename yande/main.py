# -*- coding: UTF-8 -*-
import requests
import re

def download(img_url,pname):
    print("Downloading...")
    r = requests.get(img_url)
    #print(r.status_code) # 返回状态码
    if r.status_code == 200:
        open(pname+'.jpg', 'wb').write(r.content) # 将内容写入图片
        print("Done\n")
    else:
        print("Fail")
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
        download(pic_address[i],pic_name[i])
        with open('info.txt', "a+",encoding='utf-8-sig') as f:
            f.write('ID:{}\nsource:{}\ntags:{}\n'.format(pic_name[i],pic_author[i],pic_tag[i]))
if __name__ == '__main__':
    main(5,"breasts")#order%3Arandom