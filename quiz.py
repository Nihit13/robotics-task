


from Phygital_v0 import Phygital_v0 as phy
import time



phy.init("COM3")  # Add the COM Port Number Here
phy.pinMode("A0", "dOutput")
phy.pinMode("A2", "dOutput")
phy.pinMode("A3", "dOutput")
phy.pinMode("A4", "dOutput")
phy.pinMode("A1", "dOutput")
print("This is a quiz game ")
cor_questions = -1
game = True
while True:
	try:

		choose = input("Do you want to play quiz:")
		if choose == "yes":
			phy.dWrite("A"+str(cor_questions),0)
			cor_questions = -1

			q1 = (input("What is the capital of India"))
			if q1 == "Delhi":
				print("CORRECT ANSWER")
				phy.dWrite("A"+str(cor_questions),0)
				cor_questions += 1
			else:
				print("WRONG ANSWER")
			phy.dWrite("A"+str(cor_questions),1)
			time.sleep(1)

			q2 = input("Which city is called pink city of India:")
			if q2 == "jaipur":
				print("CORRECT ANSWER")
				phy.dWrite("A"+str(cor_questions),0)
				cor_questions +=1
			else:
				print("WRONG ANSWER")
			phy.dWrite("A"+str(cor_questions),1)

			q3 = input("Where is mount everest")
			if q3 == "nepal":
				print("CORRECT ANSWER")
				phy.dWrite("A" + str(cor_questions), 0)
				cor_questions += 1
			else:
				print("WRONG ANSWER")
			phy.dWrite("A" + str(cor_questions), 1)
			time.sleep(1)
		else:
			game = False


	except:
		if KeyboardInterrupt:
			phy.close()
			break

print("Closing")
