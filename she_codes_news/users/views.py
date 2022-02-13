from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import  CustomUserCreationForm
from .forms import CustomSignUpForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# UserCreationForm

# Sign Up View
# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('users:login')
#     template_name = 'users/login.html'


class RegisterView(CreateView):
    form_class = CustomSignUpForm
    # context_object_name = 'signup'
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

class ProfileView(CreateView):
    template_name = 'users/profile.html'
    # @login_required
    def get(self, request):
        return render(request,'users/profile.html')

# class ProfileView(CreateView):
#     form_class = ProfileForm
#     template_name = 'users/profile.html'
#     def get(self, request):
#         return render(request,'users/profile.html')

# def profile_image_view(request):
    
#     if request.method == 'POST':
#         form = ProfileForm(request.POST, request.FILES)

#         if form.is_valid():
#             form.save()
#             return redirect('success')
#     else:
#         form = ProfileForm()
#     return render(request, 'pofile_image_form.html', {'form' : form})
    
    
# def success(request):
#     return HttpResponse('successfully uploaded')