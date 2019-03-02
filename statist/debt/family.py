from toobuk.tb import Toobuk

def get() :
	__walker__ = Toobuk('statist/debt/family')
	return __walker__.get('family')

