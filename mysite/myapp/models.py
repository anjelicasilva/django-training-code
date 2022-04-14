from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def fancy_name(self):
        return self.name + "!!!"

    def dict_rep(self):
        return {'name': self.name}


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    role = models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + "_" + self.role.name

class User(models.Model):
    firstname = models.CharField(max_length=256)
    lastname = models.CharField(max_length=256)
    username = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=256)

    def __str__(self):
        return self.firstname + self.lastname

    def dict_rep(self):
        return {'firstname': self.firstname,
                'lastname': self.lastname,
                'username': self.username,
                'email': self.email,
                'password': self.password
                }

class EasterEgg(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def dict_rep(self):
        return {'name': self.name}