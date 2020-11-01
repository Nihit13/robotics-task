from Phygital_v0 import Phygital_v0 as phy
import time

phy.pinMode("A0", "dOutput")
# init
phy.init("COM3")  # Add the COM Port Number Here
phy.pinMode("A2", "dOutput")
phy.pinMode("A3", "dOutput")
phy.pinMode("A4", "dOutput")
phy.pinMode("A1", "dOutput")

def pattern1():
	phy.dWrite("A0", 1)
	phy.dWrite("A4", 1)
	time.sleep(1)
	phy.dWrite("A1", 1)
	phy.dWrite("A3", 1)
	time.sleep(1)
	phy.dWrite("A2", 1)
	time.sleep(1)

	phy.dWrite("A0", 0)
	phy.dWrite("A4", 0)
	time.sleep(1)
	phy.dWrite("A1", 0)
	phy.dWrite("A3", 0)
	time.sleep(1)
	phy.dWrite("A2", 0)
	time.sleep(1)

def pattern2():
	phy.dWrite("A0", 1)
	time.sleep(1)
	phy.dWrite("A4", 1)
	time.sleep(1)
	phy.dWrite("A1", 1)
	time.sleep(1)
	phy.dWrite("A3", 1)
	time.sleep(1)
	phy.dWrite("A2", 1)
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

def pattern3():
	for y in range(5):
		for i in range(4):
			phy.dWrite("A" + str(y), 1)
			time.sleep(0.5)
			phy.dWrite("A" + str(y), 0)
			time.sleep(0.5)
		phy.dWrite("A" + str(y), 1)


	for x in range(5):
		phy.dWrite("A" + str(x), 0)
while True:
	try:
		pattern = input("Choose a pattern:")
		if pattern == "1":
			pattern1()
		elif pattern == "2":
			pattern2()
		elif pattern == "3":
			pattern3()



	except:
		if KeyboardInterrupt:
			phy.close()
			break

print("Closing")
