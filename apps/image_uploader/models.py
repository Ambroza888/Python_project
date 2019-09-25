from django.db import models
import re
from django.utils import timezone
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)




class UserManager(models.Manager):
  def basic_validator_user(self, postData):
    errors = {}
    if len(postData['name']) < 2:
      errors['name'] = "The name needs to be more than 2 characters BRAAA"
    if len(postData['alias']) < 2:
      errors['alias'] = "Choose better nickname BRa"
    if postData['password'] != postData['re_password']:
      errors['password'] = "Your password is not matching put some glasses"
    if len(postData['password']) < 5:
      errors['password'] = "Your password need to be more than 5 characters"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(postData['email']):
      errors['email'] = "Your email address is not in the right order don't cheat on my front end please !"
    return errors

class User(models.Model):
  name = models.CharField(max_length=255)
  alias = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()


class Image(models.Model):
  image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
  user = models.ForeignKey(User, related_name="images")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  

