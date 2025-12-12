# auto_email_sender.py
import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Automatic Report"
msg["From"] = "you@example.com"
msg["To"] = "client@example.com"
msg.set_content("Here is your automated report.")

with open("report.pdf", "rb") as f:
    msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="report.pdf")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("you@example.com", "PASSWORD")
    smtp.send_message(msg)
