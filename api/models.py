from django.db import models
import string
import random

def generateUniqueCode():

    while True: # generate random codes until one is unique
        code = ''.join(random.choices(string.ascii_uppercase, k = 8))
        if Room.objects.filter(code = code).count() == 0:
            break

    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length = 8, default = '', unique = True) 