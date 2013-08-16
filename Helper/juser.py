import jhelp
# userInfo.json
# [{"book": "92943.5", "name": "shayan", "cash": "0"}]

def getUserData():
	user = jhelp.readData('userInfo.json')
	jhelp.closeUpPlease('userInfo.json')
	return user

def updateCash(cash):
	user = getUserData()
	user['cash'] = cash
	jhelp.writeData('userInfo.json',user)
	jhelp.closeUpPlease('userInfo.json')

def updateCashSell(cash):
	user = getUserData()
	portMoney = float(user['cash'])
	user['cash'] = portMoney + float(cash)
	jhelp.writeData('userInfo.json',user)
	jhelp.closeUpPlease('userInfo.json')

def getCashInAccount():
	return float(getUserData()['cash'])

def resetCashPosition():
	user = getUserData()
	updateCash(100000)