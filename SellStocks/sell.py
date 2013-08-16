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

def initiateSellingSequenceNOW():
	data = jhelp.readData('data.json')
	array = getInput(data)
	while(array[1] == 0):
		array = getInput(data)
	tick = array[0]
	shares = array[1]

	numberOfSharesForStock = 0
	for ob in data:
		if(ob['tick'] == tick):
			numberOfSharesForStock += int(ob['shares'])

	if(shares > numberOfSharesForStock):
		print "You are trying to sell more shares than you have!"
	else:
		if(shares == numberOfSharesForStock):
			sellAllTheShares(tick,shares,data)
		else:
			sellSomeShares(tick,shares,data)

def getInput(data):
	array = []
	for ob in data:
		print "Ticker: " + helperMethods.bcolors.BLUE + ob['tick'] +helperMethods.bcolors.ENC + "\nShares: " + str(ob['shares'])
	sys.argv = raw_input(helperMethods.bcolors.GREEN + "Ticker To Sell: " + helperMethods.bcolors.ENC)
	name = str(sys.argv)
	array.append(name)
	sys.argv = raw_input(helperMethods.bcolors.GREEN + "Number Of Shares: " + helperMethods.bcolors.ENC)
	shares = int(sys.argv)
	array.append(shares)

	if(shares <= 0):
		array[1] = 0
		return array
	return array


# Selling all the shares
# Calculate the selling price. Take the sale price and subtract the commission.
# Remove the stock from the stockInfo.json
# take the proceeds, and add it to shayan's info. ie. increase the cash holding. 
# Show them how much cash they have.
def sellAllTheShares(tick,shares,data):
	sellingPrice = helperMethods.getPriceOfStock(tick)
	moneyMade = (sellingPrice * float(shares)) - 30
	juser.updateCashSell(moneyMade)
	jhelp.removeObjectFromData(tick,data)

def sellSomeShares(tick,shares,data):
	sellingPrice = helperMethods.getPriceOfStock(tick)
	makeDeMoney = (sellingPrice * float(shares)) - 30
	juser.updateCashSell(makeDeMoney)
	jhelp.removePartsOfObjectFromData(tick,shares,data)



