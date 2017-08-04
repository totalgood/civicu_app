""" Profile model with first and last name an image or profile description

Models:
  Label model with image ID and classification and user id
  Image model with image ID and path to the image on a shared server or a binary blob of the image itself

References:
  [Django tutorial part 1](https://docs.djangoproject.com/en/1.11/intro/tutorial01/)
  [Django tutorial part 2](https://docs.djangoproject.com/en/1.11/intro/tutorial02/)
  [Pattern for uploading files](http://www.bogotobogo.com/python/Django/Python_Django_Image_Files_Uploading_Example.php)
"""
from django.db import models

from django.contrib.auth.models import User


def user_images_directory(instance, filename):
    """ Prepend a directory path to uploaded filenames to prevent multiple files being uploaded with the same name

    If the same user uploads thes same filename twice the original file is overwritten.
    The FileField object places all uploaded files in MEDIA_ROOT/uid_<uid>/<filename>
    """
    return 'images/uid_{uid}/{filename}'.format(
        uid=getattr(instance.uploaded_by, 'id', 0),
        filename=filename)


class Image(models.Model):
    """ A database record for uploaded images to be labeled """
    caption = models.CharField("Description of the image, where and when it was taken",
                               max_length=512, default=None, null=True)  # , required=False)
    # taken_date = models.DateTimeField('Date photo was taken.', null=True, default=None)
    # updated_date = models.DateTimeField('Date photo was changed.', auto_now=True)
    # created_date = models.DateTimeField('Date photo was uploaded.', auto_now_add=True)
    uploaded_by = models.ForeignKey(User, default=None, null=True)  # , required=False)
    file = models.FileField("Select file to upload", upload_to='images')


class UserLabel(models.Model):
    """ Individual user labels (their filled out ballot, voting for a label for an image) """
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User, default=None, null=True)


class TotalVotes(models.Model):
    """ Aggregated votes (by all users, who are allowed to vote multiple times) for an individual Image """
    image = models.ForeignKey(Image, default=None, null=True)
    name = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)
