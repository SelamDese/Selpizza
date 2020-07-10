from django.http import HttpResponse
from django.shortcuts import render
from .models import Category,Regular_pizza,Sicilian_pizza,Topping,Sub,Pasta,Salad,Dinner_platter

# Create your views here.
def index(request):
    # return HttpResponse("hello")
    context = {
        "Category": Category.objects.all()
    }
    return render(request,"index.html",context)