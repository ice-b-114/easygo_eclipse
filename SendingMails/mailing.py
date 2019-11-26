#coding=utf-8
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

class Mail:   
    
    def __init__(self,sender,sender_name,password,user,subject):
        #发送人地址，发送人名字，发送人密码，收件人地址，标题
        self.sender = sender
        self.sender_name = sender_name
        self.password = password
        self.user = user
        self.subject = subject
    
    def mailphoto(self):
        msgRoot = MIMEMultipart('related')
        msgRoot['From']=formataddr([self.sender_name,self.sender])  
        msgRoot['To']=self.user
        msgRoot['Subject'] = Header(self.subject, 'utf-8')
         
        msgAlternative = MIMEMultipart('alternative')
        msgRoot.attach(msgAlternative)
         
        #邮件正文 
        mail_msg = """
            <body>
                <image src="cid:image1"></image>
            </body>
        """
        msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
        # 指定图片目录
        fp = open('advertise.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
        # 定义图片 ID，在 HTML 文本中引用
        msgImage.add_header('Content-ID', '<image1>')
        msgRoot.attach(msgImage)
        
        ret=True
        try:
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender,self.user,msgRoot.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        if ret:
            print("{0}邮件发送成功".format(self.user))
        else:
            print("{0}邮件发送失败".format(self.user))
        #os.system('pause')
    
    def mailtext(self):
        maintext = """邮件测试
        """
        
        message = MIMEText(maintext,'plain','utf-8')
        message['From']=formataddr([self.sender_name,self.sender])  
        message['To']=self.user
        message['Subject'] = Header(self.subject, 'utf-8')
        
        ret=True
        try:
            server=smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
            server.login(self.sender, self.password)  # 括号中对应的是发件人邮箱账号、邮箱密码
            server.sendmail(self.sender,self.user,message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
            server.quit()  # 关闭连接
        except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            ret=False
        if ret:
            print("{0}邮件发送成功".format(self.user))
        else:
            print("{0}邮件发送失败".format(self.user))
        #os.system('pause')
            
if __name__  ==  '__main__':
        for u in ["617656284@qq.com",]:
            new_mail = Mail("617656284@qq.com","我自己","kwdozmprbyhzbbdf",u,"测试邮件")
            #发送人地址，发送人名字，发送人密码，收件人地址，收件人名字，标题
            new_mail.mailtext()