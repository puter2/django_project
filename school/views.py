from django.http import HttpResponse
from django.shortcuts import render
from school.models import Room, Reservation
import datetime

# Create your views here.

def test_view(request):
    return HttpResponse('elo')

def home(request):
    rooms = Room.objects.all()
    reservations = Reservation.objects.filter(date=datetime.datetime.now().date())
    reservations = [res.room_id for res in reservations]
    return render(request,'homepage.html',{'rooms':rooms, 'reservations':reservations})

def add_room(request):
    if request.method == 'GET':
        return render(request, 'add_room_form.html')
    else: #POST
        name = request.POST.get('name')
        cap = request.POST.get('capacity')
        projector = request.POST.get('projector', False)
        print('tu jestem')
        print(projector)
        room = Room.objects.create(name=name, capacity=cap, projector=projector)
        return render(request, 'add_room_form.html',{'added':True})


def edit_room(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'edit_room.html',{'room': room})

