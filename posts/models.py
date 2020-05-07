from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
import datetime



class post(models.Model):
    
    ACCEPT = 2
    DENY = 3
    PENDING = 1
    CONFIRMED = 4
    STATUS_CHOICES = (
        (ACCEPT, 'accept'),
        (DENY, 'deny'),
        (PENDING, 'pending'),
        (CONFIRMED,'confirmed')
    )
    
    author = models.ForeignKey(User, related_name = 'author', on_delete = models.CASCADE)
    shift = models.ForeignKey('website.shift', null = False, related_name = 'creator_shift', on_delete = models.CASCADE)
    recipient_shift = models.ForeignKey('website.shift', blank = True , related_name = 'recipient_shift' ,on_delete = models.CASCADE, null = True)
    recipient = models.ForeignKey(User, related_name = 'recipient' ,on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)
    date_posted = models.DateTimeField()
    status = models.PositiveSmallIntegerField(choices = STATUS, default = 1)
    is_read = models.BooleanField(default = False)
    
    def __str__(self):
        date = self.date_posted.strftime("%m/%d/%Y")
        return (str(self.author) + ' - ' + str(self.recipient) + ' - ' + date)
        
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})