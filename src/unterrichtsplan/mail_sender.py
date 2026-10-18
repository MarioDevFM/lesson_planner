import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
import logging

def sent_mail(plan: str) -> None:

    MAIL = os.getenv(key='MAIL')
    PW = os.getenv(key='MAIL_PW')
    RECEIVER_MAIL = os.getenv(key='RECEIVER_MAIL')

    if MAIL is None or PW is None or RECEIVER_MAIL is None:
        raise RuntimeError(
            "The MAIL, MAIL_PW, and RECEIVER_MAIL environment variables must be set."
        )

    # Create the email.
    msg = EmailMessage()
    msg.set_content(plan)
    msg["Subject"] = "Lesson Plan Freddy"
    msg["From"] = MAIL
    msg["To"] = RECEIVER_MAIL

    # Send using a TLS-secured connection.
    try:
        with smtplib.SMTP("mail.gmx.net", port=587) as connection:
            connection.starttls()  # Encrypt the connection before authentication.
            connection.login(user=MAIL, password=PW)
            connection.send_message(msg)
            logging.info("Email sent")

    except Exception as e:
        print(f"Failed to send email: {e}")

    return None
