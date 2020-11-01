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

		phy.dWrite("A0",1)
		time.sleep(1)
		phy.dWrite("A4",1)
		time.sleep(1)
		phy.dWrite("A1",1)
		time.sleep(1)
		phy.dWrite("A3",1)
		time.sleep(1)
		phy.dWrite("A2",1)
		time.sleep(1)

		phy.dWrite("A0", 0)
		time.sleep(1)
		phy.dWrite("A4", 0)
		time.sleep(1)
		phy.dWrite("A1", 0)
		time.sleep(1)
		phy.dWrite("A3", 0)
		time.sleep(1)
		phy.dWrite("A2", 0)
		time.sleep(1)






	except:
		if KeyboardInterrupt:
			phy.close()
			break

print("Closing")
