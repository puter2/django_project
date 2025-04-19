from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=64)
    capacity = models.IntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return self.name
