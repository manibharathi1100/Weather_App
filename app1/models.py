from django.db import models


class RegisterModel(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    phone = models.BigIntegerField()
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    file = models.FileField()

    def __str__(self):
        return self.firstname


