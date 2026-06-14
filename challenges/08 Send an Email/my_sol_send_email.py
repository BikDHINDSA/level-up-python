import smtplib
from email.message import EmailMessage
sender_email = input("enter your email!!!")
sender_password = input("enter your app password!!!")
def send_email(recip_email,subject,message_body):
  msg = EmailMessage()
  msg['Subject']=subject
  msg['From']= sender_email
  msg['To'] = recip_email
  msg.set_content(message_body)
  with smtplib.SMTP('smtp.gmail.com',587) as server:
    server.starttls()
    smtp.login(send_email,sender_password)
    smtp.send_message(msg)
    