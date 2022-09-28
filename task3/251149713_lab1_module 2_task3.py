from socket import *
import ssl, base64
subject = "STMP mail sent from py"
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = ('smtp.gmail.com', 587)


# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start 
# 25 is regular mail 
# 465 is gmails ssl
# 587 is gmails TLS
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(mailserver)

#Fill in end

recv = clientSocket.recv(1024).decode() 
print('1: '+ recv)
if recv[:3] != '220':
    print('220 reply not received from server.1')



# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print('2: '+ recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.2')

tlsCommand = 'STARTTLS\r\n'
clientSocket.send(tlsCommand.encode())
recva = clientSocket.recv(1024).decode()
print("a: " + recva)
if recva[:3] != '220':
   print('220 reply not received from server.a')

#clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_SSLv23) 
clientSocket = ssl.wrap_socket(clientSocket, ssl_version=ssl.PROTOCOL_TLSv1)

#auth login
authMsg = "AUTH PLAIN\r\n"
clientSocket.send(authMsg.encode())
recvb = clientSocket.recv(1024).decode()
print("b: " + recvb)
if recvb[:3] != '250':
    print('250 reply not received from server.b')


username = "ahmadzaidsami"
password = "AhmadZaidSami2014"
auth = username + "\0" + password
base64_str = ('%s\0%s' % (username, password)).encode()
auth = base64.b64encode(base64_str)
clientSocket.send(auth)
recvy = clientSocket.recv(1024).decode()
print("y: " + recvy)
if recvy[:3] != '250':
    print('250 reply not received from server.y')



# enter sender's gmail adress below
sender = 'ahmadzaidsami@gmail.com'


# Send MAIL FROM command and print server response.
 
mailFromCommand = 'MAIL FROM: <'+ sender +'>\r\n' 
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode() 
print('3: '+ recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.3')


# enter receiver's gmail adress below
receiver = 'ahmadzaidsami@gmail.com'

# Send RCPT TO command and print server response.

# Fill in start
rcptToCommand = 'RCPT TO: <'+ receiver +'>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode() 
print('4: '+ recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.4')
# Fill in end




# Send DATA command and print server response.

# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode() 
print('5: '+ recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.5')

msgCommand = "Subject: " + subject + "\r\n\r\n" + msg +"\r\n"+ endmsg +"\r\n"
clientSocket.send(msgCommand.encode())
recv5 = clientSocket.recv(1024).decode() 
print('6: '+ recv5)
if recv5[:3] != '354':
    print('354 reply not received from server.6')

# Fill in end




# Send message data.(auth)354

# Fill in start




# Fill in end

# Message ends with a single period.

# Fill in start

# Fill in end




# Send QUIT command and get server response.221

# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode() 
print('7: '+ recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.7')
clientSocket.close()


# Fill in end
