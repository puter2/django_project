from http.client import responses

from django.http import HttpResponse
from django.shortcuts import render, redirect
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
        room = Room.objects.create(name=name, capacity=cap, projector=projector)
        return render(request, 'add_room_form.html',{'added':True})


def edit_room(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'edit_room.html',{'room': room})

def delete_room(request, id):
    room = Room.objects.get(id=id)
    if request.method=='GET':
        return render(request, 'delete.html', {'room': room})
    else: #POST
        response = request.POST.get('choice')
        if response == 'yes':
            room.delete()
        return redirect('/')

def add_res(request, id):
    room = Room.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'add_reservation.html', {'room': room})
    else: #POST
        date = request.POST.get('date')
        reserved_for_that_day = Reservation.objects.filter(date=date, room_id=room)
        if reserved_for_that_day:
            return render(request, 'add_reservation.html', {'room': room, 'message': 'this date is occupied, choose another'})
        new_res = Reservation.objects.create(date=date, room_id=room)
        return redirect('/')