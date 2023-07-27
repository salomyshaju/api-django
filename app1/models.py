from django.db import models

# Create your models here.

class premium(models.Model):
    card=models.CharField(max_length=250)
    cvv=models.CharField(max_length=250)
    email=models.EmailField()
    password=models.CharField(max_length=250)

class prem(models.Model):
    ard=models.CharField(max_length=250)
    vv=models.CharField(max_length=250)
    mail=models.EmailField()
    assword=models.CharField(max_length=250)

class pair(models.Model):
    rd=models.CharField(max_length=250)
    v=models.CharField(max_length=250)
    ail=models.EmailField()
    ssword=models.CharField(max_length=250)

class products(models.Model):
    title=models.CharField(max_length=250)
    image=models.ImageField(upload_to="pics")
    desc=models.TextField()