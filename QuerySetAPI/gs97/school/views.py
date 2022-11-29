from django.shortcuts import render
from .models import Student

# Create your views here.
def home(request):
    student_data = Student.objects.get(pk=1)
    #student_data = Student.objects.first()
    #student_data = Student.objects.order_by('name').first()
    #student_data = Student.objects.last()
    #student_data = Student.objects.order_by('name').last()
    #student_data = Student.objects.latest('pass_date')
    #student_data = Student.objects.earliest('pass_date')
    # student_data = Student.objects.all()
    # print(student_data.exists())
    # student_data = Student.objects.all()
    # one_data = Student.objects.get(pk=1)
    # print(student_data.filter(pk=one_data.pk).exists())
    #student_data = Student.objects.create(name='sameer',  roll=111, city='shindewadi', marks=85, pass_date='2022-11-23')
    #student_data, created = Student.objects.get_or_create(name='sameer',  roll=111, city='shindewadi', marks=85, pass_date='2022-11-23')
    #print(created)
    # student_data, created = Student.objects.get_or_create(name='prasad',  roll=112, city='khunte', marks=80, pass_date='2022-10-23')
    # print(created)
    #student_data = Student.objects.filter(id=11).update(name='sagar', marks=80)
    #student_data = Student.objects.filter(marks=75).update(city='pass')
    #student_data = Student.objects.update_or_create(id=12, name='prasad', defaults={'name':'kohli'})
    # objs = [
    #     Student(name='sahil', roll=113, city='phaltan', marks=85, pass_date='2022-10-23'),
    #     Student(name='gaurav', roll=114, city='pune', marks=30, pass_date='2022-09-03'),
    #     Student(name='shivtej', roll=115, city='baramti', marks=55, pass_date='2022-08-21'),
    # ]
    # student_data = Student.objects.bulk_create(objs)

    # all_student_data = Student.objects.all()
    # for stu in all_student_data:
    #     stu.city = 'phaltan'
    # student_data = Student.objects.bulk_update(all_student_data, ['city'])

    # student_data = Student.objects.in_bulk([1, 2])
    # print(student_data[2].name)

    #student_data = Student.objects.get(pk=14).delete()
    #student_data = Student.objects.filter(marks=50).delete()
    #student_data = Student.objects.all().delete()

    # student_data = Student.objects.all()
    # print(student_data.count())

    print()
    print('return: ', student_data)
    print()
    return render(request, 'school/home.html', {'student': student_data})