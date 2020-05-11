from django.db import models
from django.contrib.auth.models import  AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
#
# from django.contrib.auth.models import User
class Roles(models.Model):
  
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    #username = models.CharField(max_length=250, null=True, unique = True)
    #USERNAME_FIELD = 'username'
    pass 



class Profile(models.Model):
    name = models.CharField(max_length = 20)
    roles = models.ManyToManyField(Roles)
    district = models.PositiveIntegerField(default = 0)
    age = models.BooleanField(default=False)
    gen_manager = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=70, unique = True)
    phone_num = PhoneNumberField(unique = True, blank = True)

    def get_roles(self):
        roles = Roles.objects.get(profile__name = self.name)
        return roles

    def __str__(self):
        return self.name

    

