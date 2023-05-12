import smtplib
from email.message import EmailMessage


def send_via_smtp(message: EmailMessage, username: str = 'pinkiwinkiwinki555@gmail.com', password: str = '1234pinki'):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.login(user=username, password=password)
    s.send_message(message)
    s.quit()
