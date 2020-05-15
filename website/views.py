from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView
)
from django.db.models import Q
from .models import schedule ,shift
from users.views import Profile
from datetime import datetime
class scheduleListView(LoginRequiredMixin,ListView):
    model = schedule
    template_name = 'website/home.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        user = self.request.user
        schedule_list = schedule.objects.filter(user = user)
        #sched = schedule_list.order_by('-date_started')
        return schedule_list

class scheduleDetailView(DetailView):
    model = schedule

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(scheduleDetailView, self).get_context_data(**kwargs)
        context['shifts'] = shift.objects.filter(schedule__user = user, schedule = self.kwargs.get('pk')).order_by('-day')
        return context

class shiftDetailView(DetailView):
    model = shift      
    template_name = 'website/shift_detail.html'
    context_object_name = 'shift'

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})


