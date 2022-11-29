from django.shortcuts import render
from .forms import StudentRegistration, TeacherRegistration

# Create your views here.
def student_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/student.html', {'form':fm})

def teacher_show(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = TeacherRegistration()
    else:
        fm = TeacherRegistration()
    return render(request, 'enroll/teacher.html', {'form':fm})