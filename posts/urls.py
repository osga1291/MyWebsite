from django.urls import path
from . import views
from posts.views import(
    postSentListView,
    postReceivedListView,
    postDetailView,
    postCreateCover
)
import posts.views as post_views

urlpatterns = [
path('sent/', postSentListView.as_view(), name = 'post-sent'),
path('received/', postReceivedListView.as_view(), name = 'post-received'),
#path('new/', postCreateView.as_view(), name = 'post-create'),
path('<int:pk>/', postDetailView.as_view(), name = 'post-detail'),
path('schedule/<int:pk>/shift/<int:alt_pk>/new_cover', post_views.postCreateCover, name = 'post-create')
]