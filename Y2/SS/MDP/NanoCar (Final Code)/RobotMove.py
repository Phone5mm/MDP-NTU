import serial, time
from btconnection import *
port = serial.Serial('/dev/ttyS0',baudrate = 115200,parity='N',stopbits=1)

def FORWARD ():
 F130 = [0x5a,0x0c,0x01,0x01,0x00,0x82,0x00,0x00,0x00,0x00,0x00,0xff]
 start = time.time()
 print("go straight")
 while True:
  port.write(serial.to_bytes(F130))
  time.sleep(0.01)
  if ((time.time()) -start) >=1.15: break
 SEND("M:F")
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
 SEND("M:B")
 time.sleep(2.1)
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
 time.sleep(1)
 SEND("M:R")

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
 time.sleep(1)
 SEND("M:L")
