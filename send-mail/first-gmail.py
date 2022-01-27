import smtplib

username = 'TBC'
password = 'TBC'()
toEmail = 'TBC'
message = 'success!'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(username,password)
server.sendmail(username, toEmail, message)