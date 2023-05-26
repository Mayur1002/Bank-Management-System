from django.db import models

# Create your models here.
class User(models.Model):
    Account_No = models.IntegerField()
    name = models.CharField(max_length=50)
    Balance = models.IntegerField()
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50, default="")

class myuser(models.Model):
    Account_No = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    Balance = models.IntegerField()
    Username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50, default="")
    def __str__(self):
        return self.name


class contact(models.Model):
    Account_No = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=254)
    phone = models.IntegerField()
    message = models.CharField(max_length=1024)
    def __str__(self):
        return self.firstname

def __str__(self):
    return self.name
