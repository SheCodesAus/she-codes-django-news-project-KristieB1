from django.contrib.auth import get_user_model
from django.db import models

CATEGORY_CHOICES = (
    ('general', 'GENERAL'),
    ('cats', 'CATS'),
    ('misc','MISC'),
    ('dogs','DOGS'),
    ('coding','CODING'),
)

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    image_url = models.URLField(default='https://picsum.photos/600')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='general')
    content = models.TextField()
