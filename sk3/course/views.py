from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def learn_django(request):
    return render(request, 'course/courseone.html',
    {'nm':'Django'})

def learn_python(request):
    cname = 'Python'
    duration = '4 months'
    seats = 10
    django_details = {'pn':cname, 'du':duration, 'st':seats}
    return render(request, 'course/coursetwo.html',django_details)