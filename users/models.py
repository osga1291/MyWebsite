from django.db import models
from django.contrib.auth.models import  AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
class Roles(models.Model):
  
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
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



    def __str__(self):
        return self.user.username

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        post_save.connect(create_user_profile, sender = User)

