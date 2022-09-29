from socket import *
import ssl
import base64

#import OpenSSL

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailServer = 'smtp.gmail.com'
mailPort = 465
#Fill in start   #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start

clientSocket = socket(AF_INET,SOCK_STREAM)
wrappedSocket = ssl.SSLContext(ssl.PROTOCOL_TLSv1).wrap_socket(sock=clientSocket)

wrappedSocket.connect((mailServer, mailPort))



recv = wrappedSocket.recv(1024).decode()
#Fill in end
print ("1: "+recv)
if recv[:3] != '220':
    print ('220 reply not received from server.1')




# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
wrappedSocket.send(heloCommand.encode())
recv1 = wrappedSocket.recv(1024).decode()
print ("2: "+recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.2')



#UP=("\000"+Username+"\000"+Password).encode("base64")


auth = 'AUTH LOGIN\r\n'
wrappedSocket.send(auth.encode())
recv_from_TLS = wrappedSocket.recv(1024).decode()
print ("3: "+recv_from_TLS)
if recv_from_TLS[:3] != '334':
    print('334 reply not received from server.3')


Username=input("Insert Username: ")
Password= input('Insert Password: ')

UP = Username+"\0"+Password
base64_str = ('%s\0%s' % (Username,Password)).encode()
UP = base64.b64encode(base64_str)
wrappedSocket.send(UP)
try:
    recv_auth = wrappedSocket.recv(1024).decode()
except Exception as e: 
    print(e)

print ("a: "+recv_auth)
if recv_auth[:3] != '250':
    print('250 reply not received from server.a')


# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM: <'+ Username+'>\r\n'
wrappedSocket.send(fromCommand.encode())
recv2 = wrappedSocket.recv(1024).decode()
print ("4: "+recv2)
if recv2[:3] != '250':
    print('rcpt2 to 250 reply not received from server,  .4')
# Fill in end

# Send RCPT TO command and print server response.

receiver =input("Send email to: ")
# Fill in start
toCommand = 'RCPT TO: <'+ receiver +'>\r\n'
wrappedSocket.send(toCommand.encode())
recv3 = wrappedSocket.recv(1024).decode()
print ("5: "+recv3)
if recv3[:3] != '250':
    print('rcpt3 to 250 reply not received from server,  .5')

# Send DATA command and print server response.
# Fill in start

dataCommand = 'DATA\r\n'
wrappedSocket.send(dataCommand.encode())
recv4 = wrappedSocket.recv(1024).decode()
print ("6: "+recv4)
if recv4[:3] != '354':
    print('rcpt4 to 354 reply not received from server,  .6')

Subject=input("Subject: ")
# Text=input("Message: ")
subjectCommand = "Subject: "+Subject+"\r\n"+msg+ endmsg
wrappedSocket.send(subjectCommand.encode())
recv5 = wrappedSocket.recv(1024).decode()
print ("7: "+recv5)
if recv5[:3] != '250':
    print('rcpt5 to 250 reply not received from server,  .7')
#Fill in end

quitCommand = "QUIT\r\n"
wrappedSocket.send(quitCommand.encode())
recv6 = wrappedSocket.recv(1024).decode()
print ("8: "+recv6)
if recv6[:3] != '221':
    print('rcpt6 to 221 reply not received from server,  .8')
wrappedSocket.close()