from __future__ import annotations
import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
logger = logging.getLogger(__name__)
def send_email(
    html: str,
    subject: str,
    sender_email: str,
    app_password: str,
    receiver_email: str,
) -> None:
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.attach(MIMEText(html, "html"))
    with smtplib.SMTP("smtp.mail.me.com", 587) as server:
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
    logger.info("Email sent to %s", receiver_email)
