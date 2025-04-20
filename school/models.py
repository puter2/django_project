from django.db import models
from django.template.defaultfilters import default


# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    date = models.DateField()