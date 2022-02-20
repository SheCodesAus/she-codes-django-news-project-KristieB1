from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime

# CATEGORY_CHOICES = (
#     ('general', 'GENERAL'),
#     ('cats', 'CATS'),
#     ('misc','MISC'),
#     ('dogs','DOGS'),
#     ('coding','CODING'),
# )

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(default=datetime.now())
    image_url = models.URLField(default='https://picsum.photos/600')
    # category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='general')
    category = models.ForeignKey(Category, null=True, blank=True,
    on_delete=models.SET_NULL, 
    related_name= "stories")
    content = models.TextField()


    def __str__ (self):
        return self.title

