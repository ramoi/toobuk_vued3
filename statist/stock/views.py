from django.shortcuts import render

def index(request) : 
	return render(request, 'stock/index.html')

# Create your views here.
def render_stock(request):
    template_data = {
        'day': [1,2,3],
        'temperature': [29,27,33]
    }
    if request.method == 'GET':
        print("get...")

    return render(request, 'stock/stock.html',template_data)
