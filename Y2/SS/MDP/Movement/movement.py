# This is still in draft code with trial and error method for calibrating move distance
import serial, time

port = serial.Serial('/dev/ttyS0',baudrate = 115200,parity='N',stopbits=1)

# For data packet, index 4+5 = 16 bit for SPEED and index 8+9 = 16 bit for TURNING ANGLE.
# Let's call SPEED = X and TURNING ANGLE = Z
def FORWARD (): # reaches approximately 10cm
 F500 = [0x5a,0x0c,0x01,0x01,0x00,0x82,0x00,0x00,0x00,0x00,0x00,0xff] # X=130 and Z=0 
 for i in range (2): #1st type of loop, MIGHT change to the one with "time.time" later
  port.write(serial.to_bytes(F500)) # write data packet into the port 
  time.sleep(0.5) # time buffer, I still don't understand how this affects totol run time...

def REVERSE (): # X = -130,  reaches approximately 10cm
 R500 = [0x5a,0x0c,0x01,0x01,0xff,0x7e,0x00,0x00,0x00,0x00,0x00,0xff]
 for i in range (4):
  port.write(serial.to_bytes(R500))
  time.sleep(0.5)

def TURNR (): # Robot will end up in the same place after turning. Need allowance of 10cm to the left of starting place.
 turnR = [0x5a,0x0c,0x01,0x01,0x00,0x64,0x00,0x00,0xfc,0x18,0x00,0xff] # X = 100, Z = max (1000)
 Reverse = [0x5a,0x0c,0x01,0x01,0xff,0x9c,0x00,0x00,0xfc,0x18,0x00,0xff] # X = -100, Z = max (1000)
 start = time.time() #get current time to tag start time
 now = time.time() #get current time for later update

 run = True
 while run:
  port.write(serial.to_bytes(turnR)) #write turn right command
  time.sleep(0.5) #time buffer
  now = time.time() #update current time
  print(now) #test
  if (now-start) >=4: run=False #if current time is more than 4s of start time, end loop

 run=True
 while run:
  port.write(serial.to_bytes(Reverse))
  time.sleep(0.5)
  now = time.time()
  print(now)
  if (now-start) >=6.01: run=False #as we are using same start time, take 6.01s in total. But actually it's only 2s. It makes a difference between 6s and 6.01s. Still do not know why.
  
# FORWARD() #test to just move forward after reverse

 turnRv2 = [0x5a,0x0c,0x01,0x01,0x00,0x64,0x00,0x00,0xff,0x38,0x00,0xff] # X = 100, Z = -200
 run=True
 while run:
  port.write(serial.to_bytes(turnRv2))
  time.sleep(0.5)
  now = time.time()
  print(now)
  if (now-start) >=6.2: run=False #run for only 0.2s before end loop

TURNR() #function call to test