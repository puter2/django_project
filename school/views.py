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
        return render(request, 'add_room_form.html')

#TODO
def edit_room(request):
    print('a')
    id = request.GET.get('id')
    print(id)
    room = Room.objects.get(id=id)
    return render(request, 'edit_room.html',{'room': room})