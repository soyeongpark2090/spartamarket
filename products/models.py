from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    price = models.PositiveIntegerField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="products")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to='images/', blank=True)

    like_users = models.ManyToManyField(
        get_user_model(), related_name='like_articles'
    )

    def __str__(self):
        return self.title
        # return f'{self.title}-{self.content}'


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content
        # return f'{self.title}-{self.content}'
