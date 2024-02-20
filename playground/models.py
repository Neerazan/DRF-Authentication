from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits = 6,
        decimal_places = 2,
        validators = [MinValueValidator(1)]
    )
    last_updated = models.DateTimeField(auto_now=True)

