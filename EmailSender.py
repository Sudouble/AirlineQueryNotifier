# coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.163.com'
mail_user = 'xxx@163.com'
mail_pwd = 'xxx'

class EmailSender():
    def __init__(self, recievers):
        self.sender = mail_user
        self.recievers = recievers

    def send_email(self, msg):
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)
            smtpObj.login(mail_user, mail_pwd)
            print 'Login success.'

            message = MIMEText(msg, 'plain', 'utf-8')
            subject = '机票价格查询Robot'
            message['Subject'] = Header(subject, 'utf-8')

            for receiver in self.recievers:
                message['From'] = Header(self.sender, 'utf-8')
                message['To'] = Header(receiver, 'utf-8')
                smtpObj.sendmail(self.sender, receiver, message.as_string())
            print 'Email sent !'
        except smtplib.SMTPException as e:
            print e
            print "Send Failed."




