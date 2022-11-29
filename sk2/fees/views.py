from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fees_django(request):
    return HttpResponse("django fees 5000")

def fees_python(request):
    return HttpResponse("python fees 3000")

def f_django(request):
    return render(request, 'fees/feesone.html')

def f_python(request):
    return render(request, 'fees/feestwo.html')