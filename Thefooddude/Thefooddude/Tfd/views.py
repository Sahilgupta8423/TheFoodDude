from django.shortcuts import render
from django.http import HttpResponse
from . models import Restaurant, Food, Orders, Help

# Create your views here.
def index(request):
    res = Restaurant.objects.all()
    food = Food.objects.all()
    print(food)
    print(res)
    return  render(request, 'Tfd/restaurant.html', {'res' : res})
def searchMatch(query, item):
    # return True
    if query in item.name.lower():
        return True
    else:
        return False 

def search(request):
    allProd=[]
    food = Food.objects.all()
    query =request.GET.get('search')
    print(query)
    for item in food:
        print(item)
    prod =[item for item in food if searchMatch(query, item)]
    if len(prod) != 0:
        allProd.append(prod)
    print(allProd)    
    return render(request, 'Tfd/search.html', {'allProd':allProd[0]})    

def help(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        address = request.POST.get('address', '')
        textarea = request.POST.get('textArea','')
        help = Help(name=name, email=email, phone=phone, city=city, address=address, textarea=textarea)
        help.save()
        thank = True
        return render(request , 'Tfd/help.html', {'Thank':thank})
      
    return render(request , 'Tfd/help.html')    

def cart(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
        return render(request, 'Tfd/cart.html', {'thank':thank, 'id': id})
    return render(request , 'Tfd/cart.html')  

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

def profile(request):
    orders = Orders.objects.all()
    return render(request, 'Tfd/profile.html', {'orders':orders})

