from django.urls import path
from . import views
from posts.views import(
    postSentListView,
    postReceivedListView,
    postDetailView,
    postCreateView
)
urlpatterns = [
path('sent/', postSentListView.as_view(), name = 'post-sent'),
path('received/', postReceivedListView.as_view(), name = 'post-received'),
path('new/', postCreateView.as_view(), name = 'post-create'),
path('<int:pk>/', postDetailView.as_view(), name = 'post-detail')
]