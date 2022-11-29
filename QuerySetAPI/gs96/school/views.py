from django.shortcuts import render
from .models import Student, Teacher
from django.db.models import Q

# Create your views here.
def home(request):
    # Retrive All Data...
    student_data = Student.objects.all()

    # Retrive Specific Data....
    #student_data = Student.objects.filter(marks=80)

    # Retrive Not Specific data....
    #student_data = Student.objects.exclude(marks=80)

    # Retrive Order By Data.....
    #student_data = Student.objects.order_by('marks')
    #student_data = Student.objects.order_by('-marks')
    #student_data = Student.objects.order_by('?')
    #student_data = Student.objects.order_by('name')

    # Retrive Reverse data with Sclicing.......
    #student_data = Student.objects.order_by('id').reverse()
    #student_data = Student.objects.order_by('id').reverse()[:5]

    # Retrive data Values.....
    #student_data = Student.objects.values()
    #student_data = Student.objects.values('name', 'city')
    
    # Retrive Value_list data ..........
    #student_data = Student.objects.values_list()
    #student_data = Student.objects.values_list('id', 'name')
    #student_data = Student.objects.values_list('id', 'name',named=True)

    #student_data = Student.objects.using('default')

    #student_data = Student.objects.dates('pass_date','year')
    #student_data = Student.objects.dates('pass_date','month')

    ##################Second Table############################################

    # Retrive Union data.....
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.union(qs1)

    # Retrive Intersection Data......
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.intersection(qs1)

    # Retrive Difference data............
    # qs1 = Student.objects.values_list('id', 'name', named=True)
    # qs2 = Teacher.objects.values_list('id', 'name', named=True)
    # student_data = qs2.difference(qs1)

    ################### AND OR OPERATOR ############################################

    # student_data = Student.objects.filter(id=6) & Student.objects.filter(roll=106)
    # student_data = Student.objects.filter(Q(id=6) & Q(roll=106))

    #student_data = Student.objects.filter(id=4) | Student.objects.filter(roll=106)
    #student_data = Student.objects.filter(Q(id=5) | Q(roll=106))

    print()
    print("SQL Query :", student_data.query)
    print()
    print("Return: ", student_data)
    print()
    return render(request, 'school/home.html', {'students': student_data})