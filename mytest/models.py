from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# customusers/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models


class Javoblar(models.Model):
    javob = models.CharField(max_length=255)
    savol = models.ForeignKey('Savol',on_delete = models.CASCADE,null = True , blank = True)
    qiymat = models.BooleanField()

    def __str__(self):
        return self.javob

class Savol(models.Model):
    rasm = models.ImageField(upload_to='savol_images/')
    savol = models.CharField(max_length=255)
    test = models.ForeignKey('Test',on_delete = models.CASCADE,null = True , blank = True)
    def __str__(self):
        return self.savol

class Test(models.Model):
    nom = models.CharField(max_length=255)
    start = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()

    def __str__(self):
        return self.nom
    
class UReyting(models.Model):
    foydalanuvchi = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)  # Replace 'YourAppName' with the actual name of your app
    natija = models.IntegerField(default = -1)  # Assuming you want to store the percentage as a decimal
    orin = models.IntegerField(default = -1)
    savollar = models.IntegerField(default = 40)
    class Meta:
        ordering = ['-test', '-natija']
    def __str__(self):
        return f'{self.foydalanuvchi.username} - {self.test.nom} - {self.natija}%'

