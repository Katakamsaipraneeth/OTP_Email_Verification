import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
otp = random.randint(1111,9999)
months = {1:"january",2:"february",3:"march",4:"april",5:"may",
          6:"june",7:"july",8:"august",9:"september",10:"october",
          11:"november",12:"december"}
name = input("Enter Your Name: ")
date = int(input("Enter Your Date of Birth: " ))
month = int(input("Enter your Month of Birth: "))

tomail = input("Enter Mail id: ")
subject = "OTP For Verification"
boby =f"Hello {name} !\nDate of Birth: {date} - {months[month]}\n Your otp is - {otp}"

msg=MIMEMultipart()
msg['From'] = "ksaipraneeth1103@1103.com"
msg['To'] = tomail
msg['subject'] = subject
msg.attach(MIMEText(boby,'plain'))

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login("ksaipraneeth1103@gmail.com","kalh nwfe mixr vwyn")
server.send_message(msg)
server.quit()

userinput = input("Enter OTP recieved to your mail: ")
if userinput == str(otp):
    print("Otp verification successful")
else:
    print("Worng OTP entered")
