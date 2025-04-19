from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test_view(request):
    return HttpResponse('elo')

def home(request):
    return render(request,'homepage.html')

def add_room(request):
    if request.method == 'GET':
        return render(request, 'add_room_form.html')
    else: #POST
        return render(request, 'add_room_form.html')