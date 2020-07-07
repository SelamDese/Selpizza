from django.http import HttpResponse
from django.shortcuts import render
from .models import Order

# Create your views here.
def index(request):
    context = {
        "orders" : Order.object.all()
    }
    return render(request, "orders/index.html", context)

def menu(request,category):
    menu,columns=findTable(category)
    order_number=User_order.objects.get(user=request.user,status='initiated').order_number
    context = {
        "user":request.user,
        "Checkout":Order2.objects.filter(user=request.user,number=order_number),
        "Checkout_category":Order2.objects.filter(user=request.user,number=order_number).values_list('category').distinct(),
        "Total":list(Order2.objects.filter(user=request.user,number=order_number).aggregate(Sum('price')).values())[0],
        "Category": Category.objects.all(),
        "Active_category":category,
        "Menu": menu,
        "Columns":columns,
        "Topping_price": 0.00,
        "Order_number":order_number
    }
    return render(request,"menu.html",context)