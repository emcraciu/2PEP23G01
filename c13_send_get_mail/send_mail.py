import smtplib
from email.message import EmailMessage
import poplib
import imaplib


def send_via_smtp(message: EmailMessage, username: str = 'pinkiwinkiwinki555', password: str = '1234pinki'):
    s = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    s.ehlo()
    s.login(user=username, password=password)
    s.send_message(message)
    s.quit()


def get_mail_pop(pop_url: str = 'pop.googlemail.com', username: str = 'pinkiwinkiwinki555',
                 password: str = '1234pinki'):
    con = poplib.POP3_SSL(pop_url)
    con.user(username)
    con.pass_(password)
    for email_number in range(1, len(con.list()[1]) + 1):
        for msg in con.retr(email_number)[1]:
            yield msg
    con.quit()


def get_mail_imap(imap_url: str = 'imap.gmail.com', username: str = 'pinkiwinkiwinki555', password: str = '1234pinki'):
    con = imaplib.IMAP4_SSL(imap_url)
    con.login(username, password)
    con.select('Inbox')
    result, data = con.search(None, 'UNSEEN')
    for email_number in data[0].split():
        status, message_data = con.fetch(email_number, '(RFC822)')
        if status == 'OK':
            yield str(message_data[1], 'utf-8')
    con.logout()
    con.close()
