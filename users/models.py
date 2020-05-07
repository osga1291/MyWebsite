from django.db import models
from django.contrib.auth.models import  AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField

class Roles(models.Model):
  
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
    

class User(AbstractBaseUser):
    name = models.CharField(max_length = 20)
    roles = models.ManyToManyField(Roles)
    district = models.PositiveIntegerField(default = 0)
    age = models.BooleanField(default=False)
    gen_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, unique = True)
    phone_num = PhoneNumberField(unique = True, blank = True)

    def __str__(self):
        return self.user.name

    

