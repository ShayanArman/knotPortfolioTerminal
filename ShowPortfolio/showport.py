# =============================================================
import ystockquote
import time
import json
import sys
from Helper import helperMethods
from Helper import jhelp
from Helper import juser
# =============================================================

data = jhelp.readData('data.json')
jhelp.closeUpPlease('data.json')

# tick': u'WFM', u'name': u'Whole Foods Market', u'shares': u'260', u'bought': u'54.55'
# through code, entered 	ob['bookval'] = bookval
	# ob['currentPrice'] = price
	# ob['marketval'] = marketval
	# ob['percentgain'] = percentGain(bookval,marketval)

def printAllTheStocks(data,totalBook,totalMarket):
	for ob in data:
		name = str(ob['name'])
		bought = float(ob['bought'])
		price = ob['currentPrice']
		marketval = ob['marketval']
		bookval = ob['bookval']
		perGain = ob['percentgain']
		totalB = float(totalBook)
		totalM = float(totalMarket)
		helperMethods.printHeader(name,bought,price)
		helperMethods.printPercentOfBook(totalB,bookval,totalM,marketval)
		helperMethods.printPercentGain(perGain)
		helperMethods.printBorder()


#  tick': u'WFM', u'name': u'Whole Foods Market', u'shares': u'260', u'bought': u'54.55'
# initialize the data and find out the current total market value of the portfolio
def getObjectFromData():
	totalMarket = 0
	for ob in data:
		bought = float(ob['bought'])
		shares = float(ob['shares'])
		tick = str(ob['tick'])
		price = helperMethods.getPriceOfStock(tick)
		bookval = float(shares*bought)
		markvalue = float(helperMethods.marketValue(price,shares))
		ob['bookval'] = bookval
		ob['currentPrice'] = price
		ob['marketval'] = markvalue
		ob['percentgain'] = helperMethods.percentGain(bookval,markvalue)
		totalMarket += markvalue
	return totalMarket


def showPortfolioPlease():
	if(len(data) != 0):
		userInfo = juser.getUserData()
		username = str(userInfo['name'])
		totalBook = float(userInfo['book'])
		cash = float(userInfo['cash'])
		totalMarket = getObjectFromData() + cash
		helperMethods.printInitial(totalBook,totalMarket,helperMethods.percentGain(totalBook,totalMarket))
		printAllTheStocks(data,totalBook,totalMarket)
	else:
		print "You have no stocks in your portfolio, please buy some stocks"