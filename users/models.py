from django.db import models
from django.contrib.auth.models import User 


class Roles(models.Model):
  
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length=70, unique = True)
    roles = models.ManyToManyField(Roles)
    store = models.PositiveIntegerField(default = 0)
    age = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name

