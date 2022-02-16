from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic 

from .forms import  CustomUserCreationForm
from .forms import CustomSignUpForm
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.utils.decorators import method_decorator
from .forms import ProfileForm, form_validation_error
from .models import Profile

# UserCreationForm

# Sign Up View
# class SignUpView(CreateView):
#     form_class = CustomUserCreationForm
#     success_url = reverse_lazy('users:login')
#     template_name = 'users/login.html'


class RegisterView(generic.CreateView):
    form_class = CustomSignUpForm
    # context_object_name = 'signup'
    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    # def form_valid(self, form):
    #     r=super().form_valid(form)


# class ProfileView(CreateView):
#     template_name = 'users/profile.html'
#     # @login_required
#     def get(self, request):
#         return render(request,'users/profile.html')

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

# @method_decorator(login_required(login_url='login'), name='dispatch')
class ProfileView(generic.UpdateView):
    form_class = ProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('news:index')
    

    def  get_object(self, queryset=None):
        profile, created =Profile.objects.get_or_create(user=self.request.user)
        return profile
    # @login_required
    # def get(self, request):
    #     return render(request,'users/profile.html')
    # profile = None

    # def dispatch(self, request, *args, **kwargs):
    #     self.profile, __ = Profile.objects.get_or_create(user=request.user)
    #     return super(ProfileView, self).dispatch(request, *args, **kwargs)

    # def get(self, request):
    #     context = {'profile': self.profile, 'segment': 'profile'}
    #     return render(request, 'users/profile.html', context)

    # def post(self, request):
    #     form = ProfileForm(request.POST, request.FILES, instance=self.profile)

    #     if form.is_valid():
    #         profile = form.save()
    #         profile.user.first_name = form.cleaned_data.get('first_name')
    #         profile.user.last_name = form.cleaned_data.get('last_name')
    #         profile.user.email = form.cleaned_data.get('email')
    #         profile.user.save()

    #         messages.success(request, 'Profile saved successfully')
    #     else:
    #         messages.error(request, form_validation_error(form))
    #     return redirect('users:profile')