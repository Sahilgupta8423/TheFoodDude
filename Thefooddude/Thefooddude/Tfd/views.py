from django.shortcuts import render
from django.http import HttpResponse
from . models import Restaurant, Food

# Create your views here.
def index(request):
    res = Restaurant.objects.all()
    food = Food.objects.all()
    print(food)
    print(res)
    return  render(request, 'Tfd/restaurant.html', {'res' : res})

def help(request):
    return render(request , 'Tfd/help.html')    

def cart(request):
    food = Food.objects.all()
    return render(request , 'Tfd/cart.html', {'cart_items':food})  

def resView(request, myid):
    res = Restaurant.objects.filter(res_id = myid)
    food = Food.objects.filter(restaurant_id = myid)
    
    # rest = {'res':res, 'food':food}
    # print(rest)
    print(food)
    print(food[0])
    print(res)
    print(res[0])
    params = {'res' : res[0], 'food' : food}
    return render(request, 'Tfd/resView.html', params)       
