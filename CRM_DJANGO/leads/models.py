from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass



class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    Agent = models.ForeignKey("Agent", on_delete=models.CASCADE)

    def __str__(self):
        return f'fn in model :{self.first_name} '

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return f'username :{self.user}'

