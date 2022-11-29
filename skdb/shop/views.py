from django.shortcuts import render
from shop.models import Customer

# Create your views here.
def customerinfo(request):
    cstm = Customer.objects.all()
    return render(request, 'shop/customer.html', {'cst': cstm})