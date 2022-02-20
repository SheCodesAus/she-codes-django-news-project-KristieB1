from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic 

from .forms import  CustomUserCreationForm
from .forms import CustomSignUpForm
from django.views import View
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.utils.decorators import method_decorator
from .forms import ProfileForm, form_validation_error
from .models import Profile
from django.core.exceptions import PermissionDenied




class RegisterView(generic.CreateView):
    form_class = CustomSignUpForm
    # context_object_name = 'signup'
    success_url = reverse_lazy('news:index')
    template_name = 'users/signup.html'

class UserEdit(generic.UpdateView):
    form_class = CustomUserChangeForm
    model = CustomUser
    success_url = reverse_lazy('users:profile')
    template_name = 'users/userEdit.html'
    

    
    def  get_object(self, queryset=None):
      
        return self.request.user


    def get(self, request, *args, **kwargs):
        if(request.user.id ==None):
            raise PermissionDenied
        return super().get(self, request, *args, **kwargs)
  

    

    

class ProfileEdit(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'users/profileEdit.html'
    success_url = reverse_lazy('users:profile')
    

    def  get_object(self, queryset=None):
        profile, created =Profile.objects.get_or_create(user=self.request.user)
        return profile

class ProfileView(generic.DetailView):
    form_class = ProfileForm
    template_name = 'users/profile.html'
    context_object_name = 'profile'
    

    def  get_object(self, queryset=None):
        profile, created =Profile.objects.get_or_create(user=self.request.user)
        return profile
  