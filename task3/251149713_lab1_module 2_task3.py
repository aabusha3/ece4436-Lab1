from socket import *
import ssl, base64

#import OpenSSL

msg = '\r\n I love computer networks!'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = ('smtp.gmail.com', 465)
#Fill in start   #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start


clientSocket = ssl.wrap_socket(socket(AF_INET,SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23) # Create socket using SSL


clientSocket.connect(mailServer)



recv = clientSocket.recv(1024).decode()
#Fill in end
print ('1: '+recv)
if recv[:3] != '220':
    print ('220 reply not received from server.1')




# Send HELO command and print server response.

clientSocket.send('HELO Alice\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print ('2: '+recv)
if recv[:3] != '250':
    print ('250 reply not received from server.2')


clientSocket.send('AUTH LOGIN\r\n'.encode())
recv = clientSocket.recv(2048).decode()
print ('3: '+recv)
if recv[:3] != '334':
    print('334 reply not received from server.3')


name=input('Insert Username: ')
# username=base64.b64encode(name.encode()) + '\r\n'
# password= base64.b64encode(input('Insert Password: ').encode()) + '\r\n'
# app password: tdlcluliqdrqibwr

clientSocket.send(base64.b64encode(name.encode()) + '\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)

clientSocket.send(base64.b64encode(input('Insert Password: ').encode()) + '\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print(recv)



# Send MAIL FROM command and print server response.
# Fill in start
clientSocket.send('MAIL FROM: <'+ name+'>\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print ('4: '+recv)
if recv[:3] != '250':
    print('rcpt2 to 250 reply not received from server,  .4')
# Fill in end

# Send RCPT TO command and print server response.


# Fill in start
clientSocket.send('RCPT TO: <'+ input('Send email to: ') +'>\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print ('5: '+recv)
if recv[:3] != '250':
    print('rcpt3 to 250 reply not received from server,  .5')

# Send DATA command and print server response.
# Fill in start

clientSocket.send('DATA\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print ('6: '+recv)
if recv[:3] != '354':
    print('rcpt4 to 354 reply not received from server,  .6')



clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()

#Fill in end
clientSocket.send('QUIT\r\n'.encode())
recv = clientSocket.recv(1024).decode()
print ('8: '+recv)
if recv[:3] != '221':
    print('rcpt6 to 221 reply not received from server,  .8')
clientSocket.close()