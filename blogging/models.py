from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """class of post model inheriting from Model"""

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        """string representation of Post"""
        return self.title


class Category(models.Model):
    """categories of blog posts"""

    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name="categories")

    def __str__(self):
        """display of self"""
        return self.name

    class Meta:
        """class about Categories"""

        verbose_name_plural = "Categories"
