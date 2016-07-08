from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Portrait

def portrait(request):
    queryset = Portrait.objects.all()
    context = {
        'portrait' : queryset
    }
    return render(request, 'portrait.html', context)

def portrait_detail(request, id=None):
    instance = get_object_or_404(Portrait, id=id)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, 'portrait_detail.html', context)
