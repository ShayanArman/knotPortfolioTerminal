# ========// JSON READ AND WRITE METHODS \\ ========= #
import json
import operator

def readData(file):
	with open(file,'rb') as fp:
		return json.load(fp)

def writeData(file,data):
	with open(file,'wb') as fp:
		json.dump(data,fp)

def appendToPortfolio(file,tick,name,shares,bought):
	data = readData(file)
	thing = json.dumps({'tick':tick,'name':name,'shares':shares,'bought':bought})
	thing = json.loads(thing)
	data.append(thing)
	writeData(file,data)

def closeUpPlease(file):
	file = open(file)
	file.close()

def removeObjectFromData(ticker,data):
	poop = []
	poop = data
	listLength = int(len(poop))
	counter = 0
	for x in range(0,listLength):
		ob = poop[counter]
		if(ob['tick'] == ticker):
			poop.pop(counter)
		else:
			counter += 1

	writeData('data.json',poop)
	closeUpPlease('data.json')

# def removePartsOfObjectFromData(ticker,shares,data):
# 	sellShares = int(shares)
# 	for x in range(0,(len(data))):

def removePartsOfObjectFromData(ticker,shares,data):
	poop = []
	poop = readData('data.json')
	sellShares = int(shares)
	listLength = int(len(poop))
	counter = 0

	for x in range(0,listLength):
		ob = poop[counter]
		if(sellShares == 0):
			break
		if(ob['tick'] == ticker):
			obShares = int(ob['shares'])
			if(obShares <= sellShares):
				poop.pop(counter)
				sellShares -= obShares
			else:
				poop[counter]['shares'] = str(obShares - sellShares)
				sellShares = 0
		else:
			counter += 1
	writeData('data.json',poop)
	closeUpPlease('data.json')

def emptyPortfolio():
	empty = []
	writeData('data.json',empty)
	closeUpPlease('data.json')




# def removePartsOfObjectFromData(ticker,shares,data):
# 	sellShares = int(shares)
# 	for ob in data:
# 		if(sellShares == 0):
# 			print "I am at zero!"
# 		if(ob['tick'] == ticker):
# 			obShares = int(ob['shares'])
# 			if(operator.le(obShares,sellShares)):
# 				data.remove(ob)
# 				sellShares -= obShares
# 			else:
# 				ob['shares'] = str(obShares - sellShares)
# 				sellShares = 0
# 	writeData('data.json',data)
# 	closeUpPlease('data.json')