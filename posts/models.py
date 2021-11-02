from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()
# Create your models here.

class Group(models.Model):
    '''Creating groups model'''
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Title", max_length=1000)
    slug = models.SlugField("Slug", max_length=30, unique=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    '''Creating posts model'''
    title = models.CharField("Title", max_length=50)
    text = models.TextField("Text", max_length=1000)
    pub_date = models.DateTimeField("Pub_Date", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, blank=True, related_name="posts")
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    def __str__(self):
        return self.title

class Comment(models.Model):
    '''Creating comments model'''
    text = models.TextField("Text", max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    created = models.DateTimeField("Date", auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.text
