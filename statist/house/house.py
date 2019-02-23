from toobuk.tb import Toobuk

htb = Toobuk('statist/house/house')

def getTrade() :
	return htb.get('trade/date&loc&changeRate')

def getCharter() :
	return htb.get('charter/changeRate')


