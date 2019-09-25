from django.db import models
import re





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
  def basic_validator_review(self,postData):
    errors = {}
    if len(postData['name']) < 2:
      errors['name'] = "Need more than 2 characters for name"
    if len(postData['review_text']) < 2:
      errors['review_text'] = "Need more than 2 characters for Review"
    if postData['rating'] == "0":
      errors['rating'] = "Please pick a rating - Baby"
    return errors  


class User(models.Model):
  name = models.CharField(max_length=255)
  alias = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()
  image = models.ImageField(upload_to='profile_image', blank=True)


class Review(models.Model):
  name = models.CharField(max_length=45)
  text = models.TextField()
  rating = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager()