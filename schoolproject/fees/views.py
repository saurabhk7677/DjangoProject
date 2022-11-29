from decimal import DivisionByZero
from django.shortcuts import HttpResponse, render
from django.http import HttpResponse

# Create your views here.
def learn_format():
    #return HttpResponse  (f"Hello How Are You {a}.")
    for i in range(0,10):
        try:
            i = i / 0
            print(i)
            print("siccess")

        except Exception as e:
            print("exception  occured",e)    
            pass


