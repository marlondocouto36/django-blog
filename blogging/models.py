"""models"""

from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


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

class CategoryInline(admin.TabularInline):
    """ In line category """
    model = Category.posts.through
    extra = 1


class PostAdmin(admin.ModelAdmin):
    """post admin class"""
    list_display = ('title', 'author', 'created_date', 'published_date')
    search_fields = ('title', 'author__username')
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    """category admin class"""
    list_display = ('name', 'description')
    exclude = ('posts',)