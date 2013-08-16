import ystockquote

class bcolors:
	WARNING = '\033[95m'
	GREEN = '\033[92m'
	BLUE = '\033[94m'
	ENC = '\033[0m'
	def disable(self):
		self.WARNING = ''

def getPriceOfStock(symbol):
	return float(ystockquote.get_price(symbol))
		
def percentGain(bookValue,marketValue):
	if(marketValue > bookValue):
		percent_gain = ((marketValue/bookValue)-1)*100
		return percent_gain
	else:
		percent_loss = (1-(marketValue/bookValue))*100
		return (-1*percent_loss)

def percentOfBook(totalBook,bookval):
	return str((bookval/totalBook)*100)

def percentOfEquities(totalMarket,marketval):
	return str((marketval/totalMarket)*100)

def marketValue(price,shares):
    return price*shares

def printPercentOfBook(totalBook,bookval,totalMarket,marketval):
	print "Percent of book: " + percentOfBook(totalBook,bookval) + " Current percent: " + percentOfBook(totalMarket,marketval)

def printPercentGain(percentGain):
	if(percentGain < 0):
		print "Percent Loss: " + bcolors.WARNING + str(percentGain) + "%" + bcolors.ENC
	else:
		print "Percent Gain: " + bcolors.GREEN + str(percentGain) + "%" + bcolors.ENC

def printHeader(name,boughtAt,marketPrice):
	print name + ":| " + str(boughtAt) + " ---> " + str(marketPrice)

def printBorder():
	print bcolors.BLUE + "------------------------------------------------------------------------------" + bcolors.ENC

def printInitial(book,market,percentGain):
	print "TOTAL BOOK  " + str(book)
	print "TOTAL MARKET " + str(market)
	print "Total Gain in Capital: " + str(percentGain)
	print "==============================="
