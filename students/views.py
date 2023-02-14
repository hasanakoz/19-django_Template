from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Student
from .form import StudentForm

# Create your views here.

def home(request):

    context = {
        'title' : 'Course',
        'desc' : 'This is a description',
        'number' : 3511,
        'list1' : [1,2,3,4],
        'dict1': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'dict_list': [
            {'name': 'zed', 'age': 25},
            {'name': 'amy', 'age': 21},
            {'name': 'joe', 'age': 50},
        ]


    }

    return render(request, 'students/home.html', context)


def student_list(request):
    students = Student.objects.all()
    context = {
        'students' : students

    }

    return render(request, 'students/student_list.html', context)



def student_add(request):

    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('student_list')

    context = {
        'form' : form
    }

    return render(request, 'students/student_add.html', context)


def student_update(request, id):
    student = get_object_or_404(Student, id=id)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)

        
        if form.is_valid():
            form.save()
            return redirect('student_list')
    context = {
        'form' : form

    }
    return render(request, 'students/student_update.html', context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)

    context = {
        'student' : student
    }
    return render (request, 'students/student_detail.html', context)

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    context = {
        'student': student
    }
    return render(request, 'students/student_delete.html', context)
