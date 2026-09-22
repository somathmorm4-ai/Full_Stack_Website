from django.shortcuts import render
from  .models import Product
#from django.http import HttpResponse

# Create your views here.
def home(request):
    products = Product.objects.filter(is_available=True)
    return render(request,"home/index.html", {"products": products})


