from Phygital_v0 import Phygital_v0 as phy
import time

phy.pinMode("A0", "dOutput")
# init
phy.init("COM3")  # Add the COM Port Number Here
phy.pinMode("A2", "dOutput")
phy.pinMode("A3", "dOutput")
phy.pinMode("A4", "dOutput")
phy.pinMode("A1", "dOutput")

while True:
	try:
		for y in range(5):
			for i in range(4):
				phy.dWrite("A"+ str(y),1)
				time.sleep(0.5)
				phy.dWrite("A"+str(y),0)
				time.sleep(0.5)
			phy.dWrite("A"+str(y),1)
		for x in range(5):
			phy.dWrite("A"+str(x),0)


	except:
		if KeyboardInterrupt:
			phy.close()
			break

print("Closing")
