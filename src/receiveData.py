import serial
from datetime import datetime

port=serial.Serial("/dev/ttyUSB0", baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=3000)

logging = False
printing = False

wavelength = []
intensity = []

counter = 0

while True:
		line = port.readline()
		counter +=1
		if counter==20:
			decoded = line.decode("utf-8")
			decoded = decoded.rstrip()
			now = datetime.now()
			now = now.strftime("%d/%m/%y %H:%M:%S")
			file1 = open("temperature.csv", "a")  # append mode
			file1.write(now+","+decoded+"\r\n")
			file1.close()
			print(now+","+decoded+"\r\n")
			counter = 0




	
	
			
	
