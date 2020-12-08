from django.db import models

# Create your models here.

class Villian(models.Model):
    villian = models.CharField(max_length=60)
    DOB = models.DateField()

    def __str__(self):
        return self.villian