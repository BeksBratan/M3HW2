from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    comments = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
