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
        schedule_list = schedule.objects.filter(person = user)
        sched = schedule_list.order_by('-date_started')
        return sched

class scheduleDetailView(DetailView):
    model = schedule

    #def get_queryset(self):
     #   obj = super(scheduleDetailView, self).get_object(pk)
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(scheduleDetailView, self).get_context_data(**kwargs)
        context['shifts'] = shift.objects.filter(schedule__person = user, schedule = self.kwargs.get('pk')).order_by('-day')
        return context

class searchShiftListView(ListView):
    model = shift
    template_name = 'website/search_shift.html'
    context_object_name = 'shift_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        newlist = query.split(':')
        date = str(newlist[0]).replace(" ","")
        date_format = date.split('/')
        day = date_format[1]
        year = date_format[2]
        month = date_format[0]
        date_format[0],date_format[1],date_format[2] = year, month , day
        date = '-'.join(date_format)
        date = datetime.strptime(date, '%Y-%m-%d')
        role = str(newlist[-1]).replace(" ","")
        prof_list = Profile.objects.filter(Q(roles__name__contains= role) & ~Q(schedule__shift__day__contains = date))
        return prof_list


def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html', {'title': 'About'})


