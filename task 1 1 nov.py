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
		led_no = int(input("Enter a led no.:"))
		led_state = input("Enter a led_state:")
		num = 0
		if led_state == "on":
			num = 1
		else:
			num = 0
		phy.dWrite("A"+str(led_no),num)
		time.sleep(1)

	except:
		if KeyboardInterrupt:
			phy.close()
			break

print("Closing")
