from django.shortcuts import render
from statist.currency import currency 
from statist.debt import nation 
from statist.debt import family
from statist.house import  house
from django.http import JsonResponse
from django.shortcuts import redirect

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
	resultData = currency.get()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getDebt(request) :
	resultData = nation.get()

	print(resultData)

	return JsonResponse({ 'result' : resultData })

def getDebtFamily(request) :
	resultData = family.get()

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




def view_404(request):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/') # or redirect('name-of-index-url')