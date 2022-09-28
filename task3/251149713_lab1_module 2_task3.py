from socket import *
import ssl
import base64
import getpass
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
wrappedSocket = ssl.wrap_socket(clientSocket,      #Here we try to create a secure socket to that
                ssl_version=ssl.PROTOCOL_TLSv1,     #the mail server makes a handshake and create the response
                ciphers="HIGH:-aNULL:-eNULL:-PSK:RC4-SHA:RC4-MD5",
                cert_reqs=ssl.CERT_REQUIRED)

wrappedSocket.connect((mailServer, mailPort))



recv = wrappedSocket.recv(1024)
#Fill in end
print ("1: "+recv)
if recv[:3] != '220':
    print ('220 reply not received from server.1')




# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
wrappedSocket.send(heloCommand)
recv1 = wrappedSocket.recv(1024)
print ("2: "+recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.2')


Username=raw_input("Insert Username: ")
Password= getpass.getpass(prompt='Insert Password: ')


UP=("\000"+Username+"\000"+Password).encode("base64")

print (UP)
UP=UP.strip("\n")
login = 'AUTH PLAIN '+ UP + '\r\n'
print (login)
wrappedSocket.send(login)
recv_from_TLS = wrappedSocket.recv(1024)
print ("3: "+recv_from_TLS)




# Send MAIL FROM command and print server response.
# Fill in start
fromCommand = 'MAIL FROM: <'+ Username+'>\r\n'
print (fromCommand)
wrappedSocket.send(fromCommand)
recv2 = wrappedSocket.recv(1024)
print ("4: "+recv2)
if recv2[:3] != '250':
    print('rcpt2 to 250 reply not received from server, cabron.4')
# Fill in end

# Send RCPT TO command and print server response.

receiver =raw_input("Send email to: ")
# Fill in start
toCommand = 'RCPT TO: <'+ receiver +'>\r\n'
print (toCommand)
wrappedSocket.send(toCommand)
recv3 = wrappedSocket.recv(1024)
print ("5: "+recv3)
if recv3[:3] != '250':
    print('rcpt3 to 250 reply not received from server, cabron.5')

# Send DATA command and print server response.
# Fill in start

dataCommand = 'DATA\r\n'
print (dataCommand)
wrappedSocket.send(dataCommand)
recv4 = wrappedSocket.recv(1024)
print ("6: "+recv4)
if recv4[:3] != '354':
    print('rcpt4 to 354 reply not received from server, cabron.6')

Subject=raw_input("Subject: ")
# Text=raw_input("Message: ")
wrappedSocket.send("Subject: "+Subject+"\r\n"+msg+ endmsg)
recv5 = wrappedSocket.recv(1024)
print ("7: "+recv5)
if recv5[:3] != '250':
    print('rcpt5 to 250 reply not received from server, cabron.7')
#Fill in end


wrappedSocket.send("QUIT\r\n")
recv6 = wrappedSocket.recv(1024)
print ("8: "+recv6)
if recv6[:3] != '221':
    print('rcpt6 to 221 reply not received from server, cabron.8')
wrappedSocket.close()