from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AddStory, EditStory

urlpatterns = [
    path('', views.StoryList.as_view(), name='home'),
    path('stories/add_story', views.AddStory.as_view(), name='add_story'),
    path('<slug:slug>/', views.story_detail, name='story_detail'),
    path('stories/edit_story/<slug:pk>/', views.EditStory.as_view(), name='edit_story'),
    path('stories/delete_story/<slug:pk>/', views.DeleteStory.as_view(), name='delete_story'),
]