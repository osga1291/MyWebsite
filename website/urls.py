from django.urls import path
from . import views
from website.views import (
    scheduleListView,
    scheduleDetailView,
    searchShiftListView
)



urlpatterns = [
    path('', scheduleListView.as_view(), name = 'website-home'),
    path('schedule/<int:pk>/', scheduleDetailView.as_view(), name = 'schedule-detail'),
    path('about/', views.about, name='website-about'),
    path('search/', searchShiftListView.as_view(), name = 'shift-search'),
    

 
]