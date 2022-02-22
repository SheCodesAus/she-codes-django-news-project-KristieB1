from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.StorySearchView.as_view(), name='search'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('<int:pk>/update', views.EditStoryView.as_view(),name='editStory')

]

