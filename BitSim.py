#Written by: Adam Walsh
#Dec. 23, 2013
import json, urllib, requests, glob, sys, os

baseURL = "https://www.bitstamp.net/api/"
money = 1000 #number of $'s in account
BTCs = 0 #number of BTC's in account

#should add means of viewing timeline of transactions in some way
#also possibly add last line of file to hold newest values to accelerate loading speeds

def getCurrentBTCPrice():
	URL = baseURL + "ticker/"
	data = requests.get(URL).json()
	return round(float(data['last']),8)

def getCurrentTime():
	URL = baseURL + "ticker/"
	data = requests.get(URL).json()
	return data['timestamp']

def runSim(outFile): #run simulation
	try:
		if(os.stat(outFile).st_size == 0): #file is empty (no input to process)
			pass
		else: #file contains data to be processed
			processFile(outFile)
		outFileName = outFile
	except FileNotFoundError:
		outFileName = outFile + ".BTCsim"
	print("Simulation being saved to " + outFileName)
	out = open(outFileName, 'a')
	print("Simulation active.  Commands include b (buy), s (sell), i (info), h (help), and q (quit)")
	while True: #run main loop
		command = input('--> ')
		if(command == 'b'):
			amount = input("Please input the amount of BTCs you would like to buy: ")
			price = getCurrentBTCPrice()
			if(buy(float(amount), price)): #if successful write to file
				out.write("b " + str(round(float(amount),8)) + " " + str(round(price,8)) + " " + getCurrentTime() + "\n")
				print("Success!")
		elif(command == 's'):
			amount = input("Please input the amount of BTCs you would like to sell: ")
			price = getCurrentBTCPrice()
			if(sell(float(amount), price)): #write to file if successful
				out.write("s " + str(round(float(amount),8)) + " " + str(round(price,8)) + " " + getCurrentTime() + "\n")
				print("Success!")
		elif(command == 'i'):
			printCurrentInfo()
		elif(command == 'h'):
			print("\nCommands include b (buy), s (sell), i (info), h (help), and q (quit)")
		elif(command == 'q'):
			printCurrentInfo()
			print("Quitting...")
			sys.exit(0)
		else:
			print("Invalid command")

def processFile(inFile):
	i = open(inFile, 'r')
	for line in i.readlines():
		processLine(line)
	i.close()
	printCurrentInfo()

def processLine(line): #line format: (b/s) (amount) (price) (timestamp in sec.)
	if(line[0] == 'b'):
		words = line.split()
		amount = float(words[1]) #these must be cast to allow int functions (multiplication, addition, etc.)
		price = float(words[2])
		time = words[3]
		print("Simulating buy of " + str(round(amount,8)) + " BTCs @ price: $" + str(round(price,8)) + "\ttimestamp: " + time)
		buy(amount, price)
	elif(line[0] == 's'):
		words = line.split()
		amount = float(words[1])
		price = float(words[2])
		time = words[3]
		print("Simulating sale of " + str(round(amount,8)) + " BTCs @ price: " + str(round(price,8)) + "\ttimestamp: " + time)
		sell(amount, price)
	else:
		print("Invalid input file format - " + line)

def buy(amount, price):
	global money;
	global BTCs;
	if(amount*price < money):
		money -= amount * price
		BTCs += amount
		return True
	else:
		print("Buy FAILED - insufficent funds!")
		return False

def sell(amount, price):
	global money;
	global BTCs;
	if(amount > BTCs):
		print("Sell FAILED - insufficent BTCs!")
		return False
	else:
		money += amount * price
		BTCs -= amount
		return True

def printCurrentInfo():
	print("\nAccount Information Overview")
	print("USD Balance: " + str(round(money, 8)))
	print("BTC Balance: " + str(round(BTCs, 8)))
	print("\n" + "Current BTC price: " + str(getCurrentBTCPrice()));

if __name__ == '__main__':
	print ("1) Run simulator")
	print ("2) Get current BTC price")
	print ("Other functionality not yet implemented") #graphing? other stuff?
	resp = input('--> ')
	if (resp == '1'):
		s = input("Do you want to load a saved sim file? (y/n) ")
		if (s == 'y'):
			print ("Please pick a file:")
			files = glob.glob("/Users/adamwalsh/Developer/Python/*.BTCsim");
			for i in range(len(files)):
				print (str(i) + ") " + str(files[i]))
			index = int(input ('--> '))
			if (index < 0 or index > len(files)):
				print ("Invaild file choice")
				print ("Quitting...")
				sys.exit(0)
			simFile = files[index]
			runSim(simFile)
		else:
			outFile = input("Please name this simulation: (Warning: File names are not case-sensitive) ")
			runSim(outFile)
	elif (resp == '2'):
		print("Current BTC price: " + str(getCurrentBTCPrice()))
	else:
		print ("Invalid input")
		print ("Quitting...")
		sys.exit(0)

