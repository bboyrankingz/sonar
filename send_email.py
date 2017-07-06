import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email(object):

    def __init__(self, subject, email_from, email_to, smtp, password):
        self.msg = MIMEMultipart()
        self.msg = MIMEText('')
        self.msg['Subject'] = subject
        self.msg['From'] = email_from
        self.msg['To'] = email_to
        self.smtp = smtp
        self.password = password

    def send(self):
        mailserver = smtplib.SMTP(self.smtp, 587)
        mailserver.ehlo()
        mailserver.starttls()
        mailserver.ehlo()
        mailserver.login(self.msg['From'], self.password)
        mailserver.sendmail(self.msg['From'], [self.msg['To']], self.msg.as_string())
        mailserver.quit()