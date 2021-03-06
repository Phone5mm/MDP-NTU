from bluetooth import *
import os

os.system("/usr/bin/hciconfig hci0 piscan")

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("", 5))
server_sock.listen(1)
port = server_sock.getsockname()[1]
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ]                    )
print("Waiting for connection on RFCOMM channel %d" % port)
client_sock, client_info = server_sock.accept()
print("Accepted connection from ", client_info)

def RECEIVE():
 try:
  while True:
   data = client_sock.recv(1024)
   if len(data) == 0: break
   stringdata = data.decode('utf-8')
   return stringdata
 except IOError:
  pass

def SEND(data):
 client_sock.send(data)


def CLOSE():
 print("disconnected")
 client_sock.close()
 server_sock.close()
 print("Sockets closed")
