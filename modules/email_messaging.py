import smtplib
import pywhatkit as kit
from email.message import EmailMessage
from config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(receiver_email, subject, message):
    """Send an email using Gmail SMTP."""
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email
    msg["Subject"] = subject
    msg.set_content(message)
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
    return "Email sent successfully!"

def send_whatsapp(number, message):
    """Send a WhatsApp message."""
    kit.sendwhatmsg_instantly(f"+{number}", message)
    return "WhatsApp message sent!"
