from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Profile
from .forms import UserRegisterForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
class profileView(DetailView):
    model = Profile
    template_name = 'users/profile.html'

class SearchProfileView(ListView):
    model = Profile
    template_name = 'users/profile_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is None:
            object_list = Profile.objects.all()
        else:
            object_list = Profile.objects.filter(name__icontains = query)
        return object_list

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



