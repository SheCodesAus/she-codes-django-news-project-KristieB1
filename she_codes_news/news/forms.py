from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = '__all__'
        exclude = ['author']
        widgets = {
            'pub_date': forms.DateTimeInput(format=('%Y-%m-%dT%H:%M:%S'))}


