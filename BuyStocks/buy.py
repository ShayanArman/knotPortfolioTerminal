# =============================================================
import ystockquote
import time
import json
import sys
from Helper import helperMethods
from Helper import jhelp
from Helper import juser
from ShowPortfolio import showport
# =============================================================

# {"tick": "TSLA", "name": "Tesla Motors", "shares": "193", "bought": "109"}
def initiateBuyingSequenceSCOTTY():
	userInfo = juser.getUserData()
	username = str(userInfo['name'])
	totalBook = float(userInfo['book'])
	cash = int(userInfo['cash'])
	if(cash == 0):
		notEnoughCash(cash)
	else:
		hasEnoughCash(cash)

def getInput(cash):
	array = validateMe(cash)
	while (int(array[2]) == 0):
		array = validateMe(cash)
	return array

def validateMe(cash):
	print "You have %i dollars in cash." % cash
	array = []
	array.append(raw_input('Ticker: '))
	array.append(raw_input('Company Name: '))
	array.append(raw_input('Number Of Shares: '))
	price = validateCompany(array[0])
	array.append(price)
	if((price == 0) or (int(array[2]) * price > (cash - 30)) or (array[2] == 0)):
		print "EROR ERROR GET YOUR MOTHERS ERROR"
		array[2] = 0
		array[2] = int(array[2])
		return array
	return array

def notEnoughCash(cash):
	print "You have %i dollars in cash, you must sell some stocks." % cash

def hasEnoughCash(cash):
	array = getInput(cash) 
	ticker = str(array[0])
	companyname = str(array[1])
	shares = int(array[2])
	price = array[3]
	updatePortfolio(cash,ticker,companyname,shares,price)
	done()

def updatePortfolio(cash,tick,name,shares,bought):
	cash = cash - (shares*bought) - 30
	juser.updateCash(cash)
	jhelp.appendToPortfolio('data.json',tick,name,shares,bought)

def validateCompany(ticker):
	price = float(helperMethods.getPriceOfStock(ticker))
	if(price == 0):
		return 0
	return price

def done():
	print "Should have worked..."