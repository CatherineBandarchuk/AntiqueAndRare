from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    zipcode = models.CharField(max_length=6, default='000000')
    def __str__(self) -> str:
        return self.username