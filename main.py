# Создать класс для работы с почтой;
# Создать методы для отправки и получения писем;
# Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
# Переменные должны быть названы по стандарту PEP8;
# Весь остальной код должен соответствовать стандарту PEP8;
# Класс должен инициализироваться в конструкции.
# if __name__ == '__main__'
# Скрипт для работы с почтой.

import email
import imaplib
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Work_with_email:
    def __init__(self, login, password):
        self.login_ = login
        self.password_ = password

    def send_email(self, subject, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject  # тема письма
        msg.attach(MIMEText(message))

        GMAIL_SMTP = "smtp.gmail.com"
        ms = smtplib.SMTP(GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(self.login_, self.password_)
        ms.sendmail(self.login_, ms, msg.as_string())

        ms.quit()

    def recieve_email(self):
        GMAIL_IMAP = "imap.gmail.com"
        header = None

        mail = imaplib.IMAP4_SSL(GMAIL_IMAP)
        mail.login(self.login_, self.password_)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    login = 'login@gmail.com'
    password = 'qwerty'

    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'

    email = Work_with_email(login, password)

    email.send_email(subject, recipients, message)

