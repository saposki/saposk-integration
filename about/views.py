from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from . models import About

def about(request):
    queryset = About.objects.all()
    context = {
        'description': queryset,
        'title': 'about'
    }
    return render(request,'about.html', context)
