from socket import *
import ssl, smtplib

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
port = 465 
# port 465 is for ssl connections, read more here: https://support.google.com/mail/answer/7126229?hl=en#zippy=%2Cstep-change-smtp-other-settings-in-your-email-client

# Create a secure SSL context
context = ssl.create_default_context()

# Ask for username
username = input('Insert Username: ')

# message to be sent in the email
msg = '\r\n I love computer networks!\r\n'

# uses smtplib to create a SSL socket, log in, send mail, then quit
with smtplib.SMTP_SSL(mailServer, port, context=context) as clientSocket:
    clientSocket.login(username, (input('Insert Password: ')))
    clientSocket.sendmail(username, input('Send email to: '), msg)
    clientSocket.quit()
    
# end of program message
print('mail sent succesfully')