from toobuk.tb import Toobuk

__walker__ = Toobuk('statist/debt/debt')
		

def getDebt() :
	return __walker__.get('debtInfo/date&debtCp')

# def deptClass() :
# 	return __result__.get('deptClass')

# def debtCp() :
# 	return __result__.get('debtCp')

