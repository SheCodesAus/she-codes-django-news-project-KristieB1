from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup', views.RegisterView.as_view(), name='signup'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    # interger, primary key
]

error_404 = 'news.views.error_404'
# handler404 = ''.views.error_404'
error_500 = 'news.views.error_500'
# error_403 = 'news.views.error_403'
error_400 = 'news.views.error_400'


# from django.conf import settings
# from django.conf.urls.static import static
# if settings.DEBUG:
#         urlpatterns += static(settings.MEDIA_URL,
#                               document_root=settings.MEDIA_ROOT)

# from django.contrib import admin
# from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static
# from .views import *

# urlpatterns = [
# 	path('image_upload', profile_image_view, name = 'image_upload'),
# 	path('success', success, name = 'success'),
# ]

# if settings.DEBUG:
# 		urlpatterns += static(settings.MEDIA_URL,
# 							document_root=settings.MEDIA_ROOT)
