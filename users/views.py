from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile
class SearchProfileView(ListView):
    model = Profile
    template_name = 'users/profile_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Profile.objects.filter(name__icontains = query)
        return object_list

def profile(request):
    return render(request , 'users/profile.html')