from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from . models import post
from website.models import shift
from .forms import requestPost

class postSentListView(LoginRequiredMixin,ListView):
    model = post
    template_name = 'posts/post.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        user = self.request.user
        post_list = post.objects.filter(author = user)
        posts_sent = post_list.order_by('-date_posted')
        return posts_sent

class postReceivedListView(LoginRequiredMixin,ListView):
    model = post
    template_name = 'posts/post.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        post_list = post.objects.filter(recipient = user)
        post_received = post_list.order_by('-date_posted')
        return post_received

class postDetailView(DetailView):
    model = post







def postCreateCover(request, pk,alt_pk):
    shift_instance = get_object_or_404(shift , pk= alt_pk)
    user = request.user
    if request.method == 'POST':
        form = requestPost(request.POST, shift_instance = shift_instance)
        if form.is_valid():
            new_post = form.save(commit= False)
            new_post.save()
            new_post.author = user
            new_post.shift = shift_instance
            new_post.recipient = form.cleaned_data['recipient']
            new_post.comment = form.cleaned_data['comment']
            
            return redirect('')
    else:
        form = requestPost(shift_instance = shift_instance)
    return render(request, 'posts/post_form.html', {'form': form})



'''
class postCreateView(CreateView):
    form_class = requestPost
    template_name = 'posts/post_form.html'


    def form_valid(self, form):
        author = self.request.user
        my_shift = shift.objects.get(pk = self.kwargs['alt_pk'])
        self.object = form.save(commit = False)
        self.object.author = author
        self.object.shift = my_shift
        self.object.save()
        return super().form_valid(form)
'''