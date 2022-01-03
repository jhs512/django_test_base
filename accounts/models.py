from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MAN = "M", "남성"
        WOMAN = "W", "여성"

    first_name = None
    last_name = None
    name = models.CharField('이름', max_length=100)
    gender = models.CharField('성별', max_length=1, choices=GenderChoices.choices, blank=True)
    pass
