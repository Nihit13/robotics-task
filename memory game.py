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





	except:
		if KeyboardInterrupt:
			phy.close()
			break

print("Closing")
