from turtle import title
from unicodedata import category
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import Category, NewsStory
from .forms import StoryForm
from django.http import HttpResponse
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from users.models import CustomUser



class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all().order_by('pub_date')[:4]
        context['category_filter'] = Category.objects.all()
        context['author_filter'] = CustomUser.objects.all()
        # context['all_stories'] = NewsStory.objects.all()
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


# class SuccessMessageMixin:
#     success_message = 'Your story has been published'

#     def form_valid(self,form):
#         response = super().form_valid(form)
#         success_message = self.get_success_message(form.cleaned_data)
#         if success_message:
#             messages.success(self.request, success_message)
#         return response
    
#     def get_success_message(self, cleaned_data):
#         return self.success_message % cleaned_data

class AddStoryView(SuccessMessageMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    success_message = 'Your story has been published'
    # def my_view(request):
    #     if not request.user.is_authenticated:
    #         return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    def form_valid(self, form):
        form.instance.author = self.request.user
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return super().form_valid(form)

class EditStoryView(SuccessMessageMixin, generic.UpdateView):
    # form_class = StoryForm
    # context_object_name = 'storyForm'
    # template_name = 'news/createStory.html'
    # success_url = reverse_lazy('news:index')
    # success_message = 'Your story has been published'
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     success_message = self.get_success_message(form.cleaned_data)
    #     if success_message:
    #         messages.success(self.request, success_message)
    #     return super().form_valid(form)
    model = NewsStory
    fields = (
        'title',
        'category',
        'pub_date',
        'image_url',
        'content'
    )
    template_name = 'news/editStory.html'
    success_url= reverse_lazy('news:index')
    
    def has_permission(self, request):
        return request.user.is_active and request.user.is_author

    # def get_success_url(self):
    #     if self.object.app_label:
    #         return reverse('admin:app_list', kwargs={'app_label': self.object.app_label})
    #     else:
    #         return reverse('admin:index')

    def get_module(self):
        object = self.object if getattr(self, 'object', None) is not None else self.get_object()
        return object.load_module()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['isAuthor'] = self.request.user == self.object.author
        return context
       

    def get_settings_form_kwargs(self):
        kwargs = {
            'initial': self.module.settings
        }



class StorySearchView(generic.ListView):
    template_name = 'news/search.html'
    context_object_name = 'NewsStory'
    # model = NewsStory


    def get_queryset(self):
        '''Return all news stories.'''
        newest = self.request.GET.get('sort')
        category = self.request.GET.get('category')
        author = self.request.GET.get('author')
        
        object_list = NewsStory.objects.all()
        

        
        # object_list = self.model.objects.all()
        if category:
            object_list = object_list.filter(category__name__icontains=category)
        if author:
            object_list = object_list.filter(author__username__icontains=author)

        if newest=='fish':
            object_list = object_list.order_by('-pub_date')
        else:
            object_list = object_list.order_by('pub_date')

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['latest_stories'] = NewsStory.objects.all()[:4]
        # context['object_list'] = NewsStory.objects.all()
        context['category_filter'] = Category.objects.all()
        context['author_filter'] = CustomUser.objects.all()
        return context


 

    # class AllView(generic.ListView):
    #     template_name = 'news/allNews.html'
    #     context_object_name = 'all_stories'

    #     def get_queryset(self):
    #         '''Return all news stories.'''
    #         newest = self.request.GET.get('sort')
    #         dateQuery = NewsStory.objects.all()
    #         if newest=='fish':
    #             dateQuery = dateQuery.order_by('-pub_date')
    #         else:
    #             dateQuery = dateQuery.order_by('pub_date')
    #         return dateQuery

    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         # context['latest_stories'] = NewsStory.objects.all()[:4]
    #         # context['all_stories'] = NewsStory.objects.all()
    #         return context

  

    # def get_queryset(self):
    #     '''Return all news stories.'''
    #     return NewsStory.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['latest_stories'] = NewsStory.objects.filter(title__icontains=)
    #     # context['all_stories'] = NewsStory.objects.all()
    #     return context

    #    def get_context_data(self, **kwargs):
    #     context = super('object_list', self).get_context_data(**kwargs)
    #     if not self.profiles:
    #         self.profiles = Profile.objects.all()
    #     context.update({
    #         'profiles': self.profiles
    #     })
    #     return context

        # NewsStory.objects.filter(category__name__in=["General","Cats"])


    # def form_valid(self,form):
    #     response = super().form_valid(form)
    #     success_message = self.get_success_message(form.cleaned_data)
    #     if success_message:
    #         messages.success(self.request, success_message)
    #     return response
    
    # def get_success_message(self, cleaned_data):
    #     return self.success_message % cleaned_data

# def error_404(request, exception):
#     data= {}
#     return render(request, '404.html', data)

# def error_404(request, exception):

#         return render(request,'404.html')

def error_404(request, exception):
        data = {}
        return render(request,'news/404.html', data)
def error_400(request, exception):
        data = {}
        return render(request,'news/404.html', data)
def error_500(request, exception):
        data = {}
        return render(request,'news/404.html', data)

# def error_500(request, exception):
#     data= {}
#     return render(request, '500.html', data)

# def error_400(request, exception):
#     data= {}
#     return render(request, '400.html', data)

# def error_403(request, exception):
#     data = {}
#     return render(request, '403.html', data)

