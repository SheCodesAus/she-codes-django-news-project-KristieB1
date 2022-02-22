from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup', views.RegisterView.as_view(), name='signup'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profileEdit', views.ProfileEdit.as_view(), name='profileEdit'),
    path('userEdit', views.UserEdit.as_view(), name='userEdit'),
 
]

# error_404 = 'news.views.error_404'
# # handler404 = ''.views.error_404'
# error_500 = 'news.views.error_500'

# error_400 = 'news.views.error_400'

