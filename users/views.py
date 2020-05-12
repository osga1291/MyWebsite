from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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
        formUser = UserRegisterForm(request.POST)
        if formUser.is_valid():
            formUser.save()
            username = formUser.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

#@login_required
def profile(request):
    user = request.user
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile', pk = user.profile.pk)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update_forms.html', context)



