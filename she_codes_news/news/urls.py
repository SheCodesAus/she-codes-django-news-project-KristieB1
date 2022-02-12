from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', views.AllView.as_view(), name='allNews'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('<int:pk>/update', views.EditStoryView.as_view(),name='editStory')
    # interger, primary key
]

error_404 = 'news.views.error_404'
# handler404 = ''.views.error_404'
error_500 = 'news.views.error_500'
# error_403 = 'news.views.error_403'
error_400 = 'news.views.error_400'