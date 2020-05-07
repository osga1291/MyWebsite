from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime 
from django.urls import reverse
from django.core.exceptions import ValidationError
#from users.models import Roles
class mainSchedule(models.Model):
    date_started = models.DateField()
    date_end = models.DateField() 

class schedule(models.Model):
    #scheduleID = models.AutoField(primary_key = True)
    user = models.ForeignKey(User ,on_delete = models.CASCADE)
    hours = models.PositiveIntegerField(default = 0)
    main_sched = models.ForeignKey(mainSchedule , on_delete = models.CASCADE)


    def __str__(self):
        a = self.main_sched.date_started.strftime("%m/%d/%Y")
        b = self.main_sched.date_end.strftime("%m/%d/%Y")
        return a + ' - '+ b

    def get_absolute_url(self):
        return reverse('schedule-detail', kwargs={'pk': self.pk})






class shift(models.Model):
    
    #shiftID = models.AutoField(primary_key = True)
    #person = models.ForeignKey(User, on_delete = models.CASCADE)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    role = models.ForeignKey('users.Roles', on_delete = models.CASCADE)
    schedule = models.ForeignKey(schedule, on_delete = models.CASCADE)
    #def check_role(self , position , ):
    #    wrong_role = False
     #   if position not in person.Roles:
      #      wrong_role = True
        # return wrong_role
    def __str__(self):
        a = self.day.strftime("%m/%d/%Y")
        b = self.start_time.strftime("%H:%M:%S")
        c = self.end_time.strftime("%H:%M:%S")
        d = self.position
        return a + ' : ' + b + ' - ' + c +  ' : ' + str( d)
    '''    
    def check_overlap(self,start_time, end_time, fixed_start, fixed_end):
        overlap = False
        if(start_time == fixed_start or end_time == fixed_end):
            overlap = True
        elif(start_time >= fixed_start and end_time <= fixed_end) or (end_time >= fixed_start and end_time <= fixed_end):
            overlap = True
        elif (start_time <= fixed_start and end_time >= fixed_end):
            overlap = True
        return overlap
    
    def check_init(self):
        if self.end_time > self.start_time:
            raise ValidationError("End time must be after start time.")
        events = shift.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))


    #shifts = models.ForeignKey(shift, on_delete = models.SET_NULL, null = True)
'''
