import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from aiosmtpd.controller import Controller

class SimpleSMTPHandler:
    async def handle_DATA(self, server, session, envelope):
        print('Mail from:', envelope.mail_from)
        print('Mail to:', envelope.rcpt_tos)
        print('Message data:')
        print(envelope.content.decode('utf8', errors='replace'))
        return '250 Message accepted for delivery'

if __name__ == '__main__':
    controller = Controller(SimpleSMTPHandler(), hostname='localhost', port=1025)
    controller.start()


def send_phishing_email(sender_email, receiver_email, smtp_server, smtp_port, password):
    message = MIMEMultipart("alternative")
    message["Subject"] = "Urgent Account Verification Needed"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = """\
    Hi,
    Please verify your account by clicking on the link below:
    http://fake-login-page.com
    """
    html = """\
    <html>
    <body>
        <p>Hi,<br>
           Please verify your account by clicking on the link below:<br>
           <a href="http://fake-login-page.com">Verify Account</a>
        </p>
    </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")
    message.attach(part1)
    message.attach(part2)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Phishing email sent successfully!")

send_phishing_email("sender@example.com", "receiver@example.com", "localhost", 1025, "")
