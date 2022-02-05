from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.http import HttpResponse
from django.contrib import messages


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['all_stories'] = NewsStory.objects.all()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

# class AddStoryView(generic.CreateView):
#     form_class = StoryForm
#     context_object_name = 'storyForm'
#     template_name = 'news/createStory.html'
#     # success_url = reverse_lazy('news:index')
#     success_message = 'Your story has been published'
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# stuffing around with success messages 


class SuccessMessageMixin:
    success_message = 'Your story has been published'

    def form_valid(self,form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response
    
    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data

class AddStoryView(SuccessMessageMixin, CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    # success_url = reverse_lazy('news:index')
    success_message = 'Your story has been published'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)