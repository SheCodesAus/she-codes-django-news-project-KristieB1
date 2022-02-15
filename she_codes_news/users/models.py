from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext as _



class CustomUser(AbstractUser):
    pass

    def _str_(self):
        return self.username


class Profile(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    bio=models.TextField()
    avatar_url = models.URLField(default='https://picsum.photos/600')

    def __str__(self):
        return f'{self.username}\'s Profile '



