import smtplib
from email.mime.text import MIMEText
from algo import encrypt_msg

fromx = "example@gmail.com"
to = "donjoe@gmail.com"
password = "password"
subject = "ENC: Sample mail"

message = input("Enter message to send: ").strip()
encrypted_msg = encrypt_msg(message)

msg = MIMEText(encrypted_msg)
msg['Subject'] = subject
msg['From'] = fromx
msg['To'] = to

print("\nSending email ...\n")
print("----------------------------")
print("From:\t", msg['From'])
print("To:\t", msg['To'])
print("Subject:", msg['Subject'])
print("Message:\n", encrypted_msg)
print("----------------------------")
print("\nMessage sent ... ", u'\u2713')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.ehlo()
server.login(fromx, password)
server.sendmail(fromx, to, (msg.as_string()))
server.quit()
