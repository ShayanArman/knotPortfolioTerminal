# Most people water the weeds and pull out the flowers. ------- >>>>
# Water the flowers, pull out the fucking weeds. ------- >>>>
# Be patient like the mountain. And decisive like a rushing river. 
# Be disciplined in your manner, like the sun.
# Be humble, like socrates.
# ========================================================================
import ystockquote
import time
import json
import sys
from Helper import helperMethods
from Helper import jhelp
from Helper import juser	
from ShowPortfolio import showport 
from BuyStocks import buy
from SellStocks import sell
from StartOver import startOver
# ========================================================================

userInfo = {}
SHOW_PORTFOLIO = 'yes'
BUY_STOCKS     = 'buy'
SELL_STOCKS    = 'sell'
START_OVER     = 'restart'
EXIT           = 'exit'

def getInput():
    sys.argv = raw_input("See your portfolio?( yes / buy / sell / start over (restart) ): ").split()
    inputarray = sys.argv
    answer = inputarray[0]
    return answer

#----------------------------------------------------------
answer = getInput()

# show portfolio
if(answer == SHOW_PORTFOLIO):
    showport.showPortfolioPlease()

#----------------------------------------------------------

#buy
elif(answer == BUY_STOCKS):
    buy.initiateBuyingSequenceSCOTTY()

#----------------------------------------------------------

# sell
elif(answer == SELL_STOCKS):
    sell.initiateSellingSequenceNOW()

#----------------------------------------------------------

# empty the portfolio and reupdate the cash to zero
elif(answer == START_OVER):
    startOver.cleanMeUpAndCallMeNancy()

# 394 by 604
# Thinking about these stocks. 
#==============================
# Whole Foods Market -- Lots of cash. Same store growth. Great idea. 20 Billion Market capital. Big plans for growth. Canada has yet to be conquered. ---> 2
# Mosaic Capital -- Great growth. Relatively small, lots of room to grow, very little competition. Great price. ----- > 1
# Citicorp -- Becoming a more agile company, getting rid of their more cyclical parts, a long term hold. --------- > 3
# Wireless Wave Company -- GLN.TO. Great balance sheet and growth. Already saturated. Not going to make 5x money. But i like this one. ----> 3
# Lululemon -- Reached their growth, how many more malls can handle this thing? Same store sales decreasing. ------ > 3
# Telus -- Lots of debt. Little cash. Big growth in earnings to relatively low P/E. Could be a good one. Watch. ----- > 3 A bit better than the other 3s
# Nuance -- Watch this one closely. See what they do with their debt. Find out if they have any plans in the works for handling the debt. Call them maybe --- > 4 risky play watch closely
# UHAL -- Great stock. Big company. Not going to make 5x your money on this one. But relatively safe.  ------ > 3. Safe three.
# Solar City--> -- I like the idea, capital intensive company though, kinda like a bank. Anything to do with musk is expensive. ----- > 5 Upside not too much. Downside... a lot.
# IPAR -- Watch this stock. They basically sell smelly water. Great business. A little too expensive for my liking. ----- > 3 Good product. Upside not a ton. Downside not a ton. 
# TSLA-> -- Great product. Will be a major automotive company. Too expensive. ----> Really? Looooong term play. Still good. 3. 
# Grand Canyon Education --> 20 % increase year over year. Very good.