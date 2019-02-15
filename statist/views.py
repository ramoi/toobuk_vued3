from django.shortcuts import render
from statist.stock.stock import *
from statist.currency.currency import *
from statist.debt.debt import *
from statist.house import  house
from django.http import JsonResponse

def index(request) : 
	return render(request, 'stock/index.html')

# Create your views here.
def render_statist(request):
    template_data = {
        'day': [1,2,3],
        'temperature': [29,27,33]
    }
    if request.method == 'GET':
        print("get...")

    return render(request, 'stock/stock.html',template_data)

def getStock(request) :
	s = StockProgress()
	resultData = s.grumble()

	print(resultData)

	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse(resultData)

def m2(request) :
	s = Currency()
	resultData = s.grumble()

	print(resultData)

	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse({ 'result' : resultData })

def governmentDebtRatioByGdp(request) :
	s = GovernmentDebtRatio()
	resultData = s.grumble()

	print(resultData)

	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse({ 'result' : resultData })

def deptCp(request) :
	s = DebtCp()
	resultData = s.grumble()

	print(resultData)

	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse({ 'result' : resultData })

def getLoc(request) :
	resultData = house.getLoc()
	print(resultData)
	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse({ 'result' : resultData })

def getDate(request) :
	resultData = house.getDate()
	print(resultData)
	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse({ 'result' : resultData })

def getTradeIDRatio(request) :
	resultData = house.getTradeIDRatio()
	print(resultData)
	#result = { 'stock' : resultData, 'cmpr' : resultData['cmpr'] }
	return JsonResponse({ 'result' : resultData })
