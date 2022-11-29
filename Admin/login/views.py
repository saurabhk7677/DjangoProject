from tempfile import template
from django.template import loader
#from django.shortcuts import render
from django.http import HttpResponse

# # Create your views here.
# def Login_page(request):
#     return HttpResponse('<h1>This is a Login Page</h1>')

# def Examination_page(request):
#     return HttpResponse('<h1>This is a Examination Page!</h1>')

def index(request):
    template = loader.get_template("myfirst.html")
    return HttpResponse(template.render())

