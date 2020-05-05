from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
from . models import post
class postSentListView(ListView):
    model = post
    template_name = 'posts/post.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        user = self.request.user
        post_list = post.objects.filter(author = user)
        posts_sent = post_list.order_by('-date_posted')
        return posts_sent

class postReceivedListView(ListView):
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


class postCreateView(CreateView):
    model = post
    fields = ['title','shift','recipient','recipient_shift','comment']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
