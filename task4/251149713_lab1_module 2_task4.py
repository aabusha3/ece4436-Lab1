from socket import *
import ssl, base64
import smtplib


msg = '\r\n I love computer networks!' # message to send
endmsg = '\r\n.\r\n' # end-of-message signifier

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = ('smtp.gmail.com', 465)
# port 465 is for ssl connections, read more here: https://support.google.com/mail/answer/7126229?hl=en#zippy=%2Cstep-change-smtp-other-settings-in-your-email-client

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = ssl.wrap_socket(socket(AF_INET,SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23) # Create socket using SSL protocol
clientSocket.connect(mailServer)
recv = clientSocket.recv(1024).decode()
if recv[:3] == '220':
    print (recv)
else:
    print('220 reply not received from server.\n'+recv)


# Send HELO command and print server response.
clientSocket.send('HELO Alice\r\n'.encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '250':
    print (recv)
else:
    print('250 reply not received from server.\n'+recv)


# Send AUTH LOGIN command and print server response.
clientSocket.send('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(2048).decode()
if recv[:3] == '334':
    print (recv)
else:
    print('334 reply not received from server.\n'+recv)


# Ask for username and send it, then print server response.
name=input('Insert Username: ')
clientSocket.send(base64.b64encode(name.encode()) + '\r\n'.encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '334':
    print (recv)
else:
    print('334 reply not received from server.\n'+recv)


# Ask for password and send it, then print server response.
clientSocket.send(base64.b64encode(input('Insert Password: ').encode()) + '\r\n'.encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '235':
    print (recv)
else:
    print('235 reply not received from server.\n'+recv)


# Send MAIL FROM command and print server response.
clientSocket.send(('MAIL FROM: <'+ name+'>\r\n').encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '250':
    print (recv)
else:
    print('250 reply not received from server.\n'+recv)


# Send RCPT TO command and print server response.
clientSocket.send(('RCPT TO: <'+ input('Send email to: ') +'>\r\n').encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '250':
    print (recv)
else:
    print('250 reply not received from server.\n'+recv)


# Send DATA command and print server response.
clientSocket.send('DATA\r\n'.encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '354':
    print (recv)
else:
    print('354 reply not received from server.\n'+recv)


# Send message and ENDMSG signifier and print server response.
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '250':
    print (recv)
else:
    print('250 reply not received from server.\n'+recv)


# Send QUIT command and print server response, then close the connection.
clientSocket.send('QUIT\r\n'.encode())
recv = clientSocket.recv(1024).decode()
if recv[:3] == '221':
    print (recv)
else:
    print('221 reply not received from server.\n'+recv)
clientSocket.close()