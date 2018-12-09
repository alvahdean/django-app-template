from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Count
from random import randint

# Models
# The focus of the application is the concept of "posts". Posts are what users add, vote on, and comment on. 
# Each post must have one author (the user who created it), a link, and a title. 
# Each post can have a description -- longer text describing the link or asking a question.
# Posts belong to a user, the author. Posts have many comments and votes.
# Votes belong to a user, the voter, and a post.
# Comments belong to a user, the author, and a post.
# Users have many posts, comments, and votes.

class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1024)
    url = models.URLField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)
    def slug(self): return self.pk
    def __str__(self):
        return self.title

class Vote(models.Model):
    # todo: rename author to user and remove user alias
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def user(self): return self.author
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    def slug(self): return self.pk
    def __str__(self):
        return self.author.username + " - " + self.post.title
    class Meta:
        unique_together = ("author", "post")

class Comment(models.Model):
    # todo: rename author to user and remove user alias
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def user(self): return self.author
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    contents = models.TextField(max_length=1024)
    created_date = models.DateTimeField(default=timezone.now)
    def slug(self): return self.pk
    def __str__(self):
        return self.author.username + " - " + self.post.title

