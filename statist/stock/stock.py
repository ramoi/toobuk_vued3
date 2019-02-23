from toobuk.tb import Toobuk

class StockProgress(Toobuk) :
	def __init__(self) :
		self.__walker__ = Toobuk('statist/stock/stock')

	def grumble(self) :
		stockList = self.__walker__.get('stock')['stockList']
		cmprList = self.__walker__.get("cmpr") ['cmprList']

		for stock in stockList :
			parameter = { 'code' : stock['code'] }
			# stock.update( self.__walker__.get('stockDetail', parameter)['name'] )
			stock.update(self.__walker__.get('stockDetail', parameter)['name']['data'])
			print(stock)

		return { 'stock' : stockList, 'cmpr' : cmprList }

