from unicodedata import category
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from .models import Category, NewsStory
from .forms import StoryForm
from django.views.generic.edit import UpdateView
from django.contrib import messages
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect
from users.models import CustomUser
from django.http import QueryDict



class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = 'latest_stories'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')[:4]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_filter'] = Category.objects.all()
        context['author_filter'] = CustomUser.objects.all()
        return context

class AllView(generic.ListView):
    template_name = 'news/allNews.html'
    context_object_name = 'all_stories'

    def get_queryset(self):
        '''Return all news stories.'''
        newest = self.request.GET.get('sort')
        dateQuery = NewsStory.objects.all()
        if newest=='fish':
            dateQuery = dateQuery.order_by('-pub_date')
        else:
            dateQuery = dateQuery.order_by('pub_date')
        return dateQuery

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'





class AddStoryView(SuccessMessageMixin, generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    success_message = 'Your story has been published'
   
    def form_valid(self, form):
        form.instance.author = self.request.user
        
        return super().form_valid(form)

class EditStoryView(SuccessMessageMixin, generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
   
    template_name = 'news/editStory.html'
    success_url= reverse_lazy('news:index')
    success_message = 'Your story has been updated'
    
    def has_permission(self, request):
        return request.user.is_active and request.user.is_author



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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class StorySearchView(generic.ListView):
    template_name = 'news/search.html'
    context_object_name = 'NewsStory'

    def get_queryset(self):
        category = self.request.GET.get('category')
        author = self.request.GET.get('author')
        sort = self.request.GET.get('sort')

        object_list = NewsStory.objects.all()
        if category:
            object_list = object_list.filter(category__name__icontains=category)
        if author:
            object_list = object_list.filter(author__username__icontains=author)

        if sort=='asc':
            object_list = object_list.order_by('-pub_date')
        else:
            object_list = object_list.order_by('pub_date')

        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_sort = self.request.GET.get('sort')

        sort = None
        if(current_sort == 'asc'):
            q = self.request.GET.copy()
            q['sort'] = 'desc'
            sort = (q.urlencode(),'Newest')
        else:
            q = self.request.GET.copy()
            q['sort'] = 'asc'
            sort = (q.urlencode(),'Oldest')

        category = []

        for C in Category.objects.all():
            q = self.request.GET.copy()
            q['category'] = C.name
            category.append((q.urlencode(),C.name))

        author = []

        for A in CustomUser.objects.all():
            q = self.request.GET.copy()
            q['author'] = A.username
            author.append((q.urlencode(),A.username)) 

        context['category_filter'] = category 
        context['author_filter'] = author
        context['sort'] = sort

        return context


  

    

def error_404(request, exception):
        data = { 'home':reverse('news:index')}
        response = render(request,'news/404.html', data)
        response.status_code =404
        return response
def error_400(request, exception):
        data = { 'home':reverse('news:index')}
        response = render(request,'news/400.html', data)
        response.status_code =400
        return response
def error_500(request, exception):
        data = { 'home':reverse('news:index')}
        response = render(request,'news/500.html', data)
        response.status_code =500
        return response
def error_403(request, exception):
        data = { 'home':reverse('news:index')}
        response = render(request,'news/403.html', data)
        response.status_code =403
        return response


