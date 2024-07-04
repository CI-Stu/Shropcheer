from . import views
from django.urls import path

urlpatterns = [
    path('', views.StoryList.as_view(), name='home'),
]