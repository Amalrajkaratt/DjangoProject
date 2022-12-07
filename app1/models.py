from django.db import models

# Create your models here.
class Table1(models.Model):
    Name=models.CharField(max_length=16)
    Age=models.IntegerField()
    Place=models.CharField(max_length=16)
    Email=models.EmailField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Password=models.CharField(max_length=16)
    ConfirmPassword=models.CharField(max_length=16)

class Gallery(models.Model):
    Name=models.CharField(max_length=16)
    Age=models.IntegerField()
    Place=models.CharField(max_length=16)
    Email=models.EmailField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Password=models.CharField(max_length=16)
    ConfirmPassword=models.CharField(max_length=16)