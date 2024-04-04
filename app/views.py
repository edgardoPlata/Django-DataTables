from django.shortcuts import render
from .models import Programmer
from django.http import JsonResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def list_programmers(_request):
    programmers = list(Programmer.objects.values())
    data = {
        'programmers': programmers,

    }
    return JsonResponse(data)