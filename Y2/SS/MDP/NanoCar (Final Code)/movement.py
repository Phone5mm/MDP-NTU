from tryDect import Detect
m=0
import serial, time
port = serial.Serial('/dev/ttyS0',baudrate = 115200,parity='N',stopbits=1)

def FORWARD ():
 F130 = [0x5a,0x0c,0x01,0x01,0x00,0x82,0x00,0x00,0x00,0x00,0x00,0xff]
 start = time.time()
 while True:
  port.write(serial.to_bytes(F130))
  time.sleep(0.01)
  if ((time.time()) -start) >=1.15: break
 port.reset_input_buffer()
 port.reset_output_buffer()
 time.sleep(2.1)

def REVERSE ():
 R130 = [0x5a,0x0c,0x01,0x01,0xff,0x7e,0x00,0x00,0x00,0x00,0x00,0xff]
 start = time.time()
 while True:
  port.write(serial.to_bytes(R130))
  time.sleep(0.01)
  if ( (time.time())- start) >=1.15: break
 port.reset_input_buffer()
 port.reset_output_buffer()

def TURNR ():
 turnR = [0x5a,0x0c,0x01,0x01,0x00,0x64,0x00,0x00,0xfc,0x18,0x00,0xff]
 Reverse = [0x5a,0x0c,0x01,0x01,0xff,0x9c,0x00,0x00,0xfc,0x4a,0x00,0xff]
 start = time.time()
 while True:
  port.write(serial.to_bytes(turnR))
  time.sleep(0.01)
  if ((time.time())-start) >=4.2: break
 while True:
  port.write(serial.to_bytes(Reverse))
  time.sleep(0.01)
  if ((time.time())-start) >=7.1: break
 turnRv2 = [0x5a,0x0c,0x01,0x01,0x00,0x64,0x00,0x00,0x00,0x00,0x00,0xff]
 while True:
  port.write(serial.to_bytes(turnRv2))
  time.sleep(0.01)
  if ((time.time())-start) >=7.4: break
 port.reset_input_buffer()
 port.reset_output_buffer()

def TURNL():
 turnL = [0x5a,0x0c,0x01,0x01,0x00,0x64,0x00,0x00,0x03,0xe8,0x00,0xff]
 Reverse = [0x5a,0x0c,0x01,0x01,0xff,0x9c,0x00,0x00,0x01,0x58,0x00,0xff]
 start = time.time()
 while True:
  port.write(serial.to_bytes(turnL))
  time.sleep(0.01)
  if ((time.time())-start) >=4.2: break
 while True:
  port.write(serial.to_bytes(Reverse))
  time.sleep(0.01)
  if ((time.time())-start) >=7.1: break
 turnLv2 = [0x5a,0x0c,0x01,0x01,0x00,0x64,0x00,0x00,0xff,0xd8,0x00,0xff]
 while True:
  port.write(serial.to_bytes(turnLv2))
  time.sleep(0.01)
  if ((time.time())-start) >=7.45: break
 port.reset_input_buffer()
 port.reset_output_buffer()


def MOVENEXT():

 TURNR()
 time.sleep(1)

 FORWARD()
 time.sleep(2.5)

 FORWARD()
 time.sleep(2.5)

 FORWARD()
 time.sleep(2.5)

 TURNL()
 time.sleep(1)

 for k in range (4): FORWARD()
 time.sleep(3)

 TURNL()

#MOVENEXT()

#while True:
# detect=Detect()
# class_id=detect.main(m)
## print(class_id)
# if (class_id == 16 or class_id == 15): MOVENEXT()
# else: break

TURNL()

time.sleep(1)

for i in range(3):
 FORWARD()

