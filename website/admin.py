from django.contrib import admin
from .models import shift, schedule, mainSchedule
admin.site.register(shift)
admin.site.register(schedule)
admin.site.register(mainSchedule)
# Register your models here.
