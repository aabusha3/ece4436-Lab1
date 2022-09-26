from socket import *

msg = "\r\n I love computer networks!" 
endmsg = "\r\n.\r\n"


# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = 'smtp.gmail.com'
#serverName = ‘hostname’
#serverPort = 12000


# Create socket called clientSocket and establish a TCP connection with mailserver

#Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,25))

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
 
mailFromCommand = 'MAIL FROM: <mail@gmail.com>\r\n' 
clientSocket.send(mailFromCommand.encode())
recv2 = clientSocket.recv(1024).decode() 
print(recv2)
if recv2[:3] != '250':
    print('250 reply not received from server.')


# Send RCPT TO command and print server response.

# Fill in start




# Fill in end




# Send DATA command and print server response.

# Fill in start




# Fill in end




# Send message data.(auth)354

# Fill in start




# Fill in end

# Message ends with a single period.

# Fill in start

# Fill in end




# Send QUIT command and get server response.221

# Fill in start




# Fill in end
