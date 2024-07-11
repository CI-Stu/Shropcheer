from . import views
from django.urls import path
from .views import AddStory

urlpatterns = [
    path('', views.StoryList.as_view(), name='home'),
    path('stories/add_story', views.AddStory.as_view(), name='add_story'),
    path('<slug:slug>/', views.story_detail, name='story_detail'),
    
]