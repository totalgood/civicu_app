""" Profile model with first and last name an image or profile description
    Label model with image ID and classification and user id
    Image model with image ID and path to the image on a shared server or a binary blob of the image itself
"""
import os
from django.db import models

from django.contrib.auth.models import User


class Image(models.Model):
    filepath = models.CharField("Path relative to BASE_PATH for the image file",
                                max_length=512)
    caption = models.CharField("Description of the image, where and when it was taken",
                               max_length=512)
    created_date = models.DateTimeField('Date photo was taken.')
    file = models.FileField(upload_to='.')


class UserLabel(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)


class TotalVotes(models.Model):
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
