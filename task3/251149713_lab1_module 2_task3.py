from socket import *

subject = "STMP mail sent from py"
msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = 'smtp.gmail.com'

# enter user's gmail adress below
user = 'ahmadzaidsami@gmail.com'

# enter destinations's gmail adress below
receiver = 'ahmadzaidsami@gmail.com'


# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start 
# 25 is regular mail 
# 465 is gmails ssl
# 587 is gmails TLS
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,587))

#Fill in end


#############
# udp example

# get user keyboard input
# message = raw_input(’Input lowercase sentence:’)

# attach server name, port to message; send into socket
# clientSocket.sendto(message.encode(), (serverName, serverPort))

# read reply characters from socket into string
# modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print out received string and close socket
# print modifiedMessage.decode()
# clientSocket.close()
#############


recv = clientSocket.recv(1024).decode() 
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')




# Send HELO command and print server response. 
heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode() 
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')



# Send MAIL FROM command and print server response.
 
mailFromCommand = 'MAIL FROM: <'+ user +'>\r\n' 
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode() 
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')


# Send RCPT TO command and print server response.

# Fill in start
rcptToCommand = 'RCPT TO: <'+ receiver +'>\r\n'
clientSocket.send(rcptToCommand.encode())
recv3 = clientSocket.recv(1024).decode() 
print(recv3)
if recv3[:3] != '250':
    print('250 reply not received from server.')



# Fill in end




# Send DATA command and print server response.

# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode() 
print(recv4)
if recv4[:3] != '250':
    print('250 reply not received from server.')

msgCommand = "Subject: " + subject + "\r\n\r\n" + msg +"\r\n"+ endmsg +"\r\n"
clientSocket.send(msgCommand.encode())
recv5 = clientSocket.recv(1024).decode() 
print(recv5)
if recv5[:3] != '354':
    print('354 reply not received from server.')

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
print(recv6)
if recv6[:3] != '221':
    print('221 reply not received from server.')
clientSocket.close()


# Fill in end
