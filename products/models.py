from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='images/', blank=True)
