from toobuk.tb import Toobuk

__walker__ = Toobuk('statist/debt/family')
def get() :
	return __walker__.get('family')

