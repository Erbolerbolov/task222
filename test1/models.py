from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=150)


class Comment(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=150)

