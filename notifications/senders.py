import smtplib
from notifications import BaseConfig


def send_email(address: str, message: str, subject: str = ""):
    email = "\r\n".join((
        "From: %s" % BaseConfig.FROM_EMAIL,
        "To: %s" % address,
        "Subject: %s" % subject,
        "",
        message
    ))

    server = smtplib.SMTP(BaseConfig.SMTP_URI)
    try:
        server.sendmail(BaseConfig.FROM_EMAIL, [address], email)
    except smtplib.SMTPException as smtpEx:
        logging.error(smtpEx.strerror)
    finally:
        server.quit()
