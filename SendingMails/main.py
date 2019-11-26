#coding=utf-8
import mailing
import time
import _thread

def loop():
    while 1:
        for u in ["617656284@qq.com",]:
            new_mail = mailing.Mail("617656284@qq.com","我自己","kwdozmprbyhzbbdf",u,"测试邮件")
            #发送人地址，发送人名字，发送人密码，收件人地址，收件人名字，标题
            #new_mail.mailtext()
            new_mail.mailphoto()
        time.sleep(30)
        
try:
    _thread.start_new_thread(loop,()) #创建线程
except:
    print ("Error")
   

input("程序开始，按回车键结束\n")

    
    