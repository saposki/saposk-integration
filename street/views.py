from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from . models import Street

def street(request):
    queryset = Street.objects.all()
    context = {
        'street' : queryset
    }
    return render(request, 'street.html', context)

def street_detail(request, id=None):
    instance = get_object_or_404(Street, id=id)
    context = {
        'title': instance.title,
        'instance': instance
    }
    return render(request, 'street_detail.html', context)
