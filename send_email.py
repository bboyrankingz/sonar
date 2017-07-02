import smtplib
from email.mime.text import MIMEText


class Email(object):

    def __init__(self, subject, email_from, email_to, smtp):
        self.msg = MIMEText('')
        self.msg['Subject'] = subject
        self.msg['From'] = email_from
        self.msg['To'] = email_to
        self.smtp = smtp

    def send(self):
        s = smtplib.SMTP(self.smtp)
        s.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string())
        s.quit()