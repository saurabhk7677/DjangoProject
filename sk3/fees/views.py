from django.shortcuts import render
from datetime import datetime

# Create your views here.
def fees_django(request):
    django_details = {'nm': 'django is Awesome'}
    return render(request, 'fees/feesone.html', django_details)

def fees_time(request):
    d = datetime.now()
    return render(request, 'fees/feestwo.html', {'dt': d})