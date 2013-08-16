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

def cleanMeUpAndCallMeNancy():
	jhelp.emptyPortfolio()
	juser.resetCashPosition()
