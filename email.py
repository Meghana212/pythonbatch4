import smtplib

sender = "me@gmail.com"
receiver = ["friend@gmail.com"]
message = "Hello!"
try:
    session = smtplib.SMTP('smtp.gmail.com',587)
    session.ehlo()
    session.starttls()
    session.ehlo()
    session.login(sender,'mypassword')
    session.sendmail(sender,receiver,message)
    session.quit()
    print "Message successfully sent."
except smtplib.SMTPException:
       print "Error: unable to send email"
