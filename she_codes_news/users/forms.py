from pyexpat import model
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from .models import *
from .models import Profile

# Sign Up Form
class CustomSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']



class CustomUserChangeForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email')


# class CustomUserChangeForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ['first_name', 'last_name', 'email']
#         # exclude = ['password']


class ProfileForm(forms.ModelForm):

    def __init__(self,  *args, **kwargs):
        super(ProfileForm, self ).__init__(*args, **kwargs)
        
    # last_name = forms.CharField(max_length=255)
    # email = forms.EmailField()

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg