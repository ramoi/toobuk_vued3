from django.shortcuts import render
from statist.currency.currency import *
from statist.debt import debt
from statist.house import  house
from django.http import JsonResponse

def index(request) : 
	return render(request, 'stock/index.html')

# Create your views here.
# def render_statist(request):
#     template_data = {
#         'day': [1,2,3],
#         'temperature': [29,27,33]
#     }
#     if request.method == 'GET':
#         print("get...")

#     return render(request, 'stock/stock.html',template_data)

# def getStock(request) :
# 	s = StockProgress()
# 	resultData = s.grumble()

# 	print(resultData)

# 	return JsonResponse(resultData)

def getStock(request) :
	return JsonResponse( {} )

def getCurrency(request) :
	s = Currency()
	resultData = s.grumble()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getDebt(request) :
	resultData = debt.getDebt()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getTrade(request) :
	resultData = house.getTrade()
	print(resultData)
	return JsonResponse({ 'result' : resultData })

def getCharter(request) :
	resultData = house.getCharter()
	print(resultData)
	return JsonResponse({ 'result' : resultData })
