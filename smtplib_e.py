import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def get_password(user_name):
    file = open("users.txt", "r")
    sort = file.readlines()
    for i in sort:
        split = i.split()
        u_name = split[0]
        u_password = split[1]
        u_mail = split[2]
        if u_name == user_name:
            send_password_to_mail(user_name=user_name, mail=u_mail, password=u_password)


def send_password_to_mail(user_name, mail, password):
    sender_mail = "exmaple@example.com"
    sender_mail_password = "password"
    content = f"Hello {user_name}, you asked us  to send you the password " \
              f"on {datetime.now().strftime('%d %m %Y %H:%S')}" \
              f" \n Your password: {password}"
    message = MIMEMultipart()
    message["Subject"] = "password sent"
    message["From"] = sender_mail
    message["To"] = mail
    message.attach(MIMEText(content, "plain"))

    mail_service = smtplib.SMTP("smtp.gmail.com", 587)  # server
    mail_service.ehlo()
    mail_service.starttls()  # send encrypted
    mail_service.login(sender_mail, sender_mail_password)
    mail_service.sendmail(sender_mail, mail, message.as_string())
    mail_service.quit()
    print("Done")


get_password("User")
