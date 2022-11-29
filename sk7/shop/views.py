from django.shortcuts import render
from shop.models import Shopshirt

# Create your views here.
def custinfo(request):
    cust = Shopshirt.objects.all()
    return render(request, 'shop/custshopping.html', {'cust': cust})
