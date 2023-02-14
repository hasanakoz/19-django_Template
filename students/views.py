from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):

    context = {
        'title' : 'Course',
        'desc' : 'This is a description',
        'number' : 3511,
        'list1' : [1,2,3,4]

    }

    return render(request, 'students/home.html', context)

    # return HttpResponse('<h1> Hello </h1>')