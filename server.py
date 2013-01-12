import socket

s=socket.socket()
host=socket.gethostname()
port=8080;

print(host);
print('\nSERVER STARTED');
print('\nWAITNG FOR CLIENTS');

#s.bind((host,port))
#s.listen(5)
#c, addr=s.accept()

#print ('GOT CONNECTTION FORM ',addr)

#while TRUE:
 #   msg=c.recv(1024)
  #  print addr, '>>',msg
   # msg=raw_input('SERVER >>')

    
