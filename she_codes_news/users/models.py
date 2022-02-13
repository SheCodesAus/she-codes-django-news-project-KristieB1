from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass

    def _str_(self):
        return self.username


class Profile(models.Model):
    AbstractUser=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    bio=models.TextField()
  

    def __str__(self):
        return f'{self.username}\'s Profile '