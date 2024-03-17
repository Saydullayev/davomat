from django.db import models

class User(models.Model):
    ism = models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    ishdami = models.BooleanField() # bugun ishga kelganmi. True = kelgan, False kelmagan
    login = models.CharField(max_length=255) 
    password = models.CharField(max_length=255) # login va parolni ish beruvchi beradi