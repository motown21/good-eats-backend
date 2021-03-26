from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Mango(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  ripe = models.BooleanField()
  color = models.CharField(max_length=100)

  # get_user_model() returns the correct User model
  # This takes the place of `User` or `'User'`
  owner = models.ForeignKey(
    get_user_model(),
    # 'User',
    # related_name is optional
    # overrides the default field on the related model to represent
    # the relationship
    # User will have a field called `mangos` that is all the mangos w/
    # foreignKeys pointing to the user
    related_name='mangos',
    on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The mango named '{self.name}' is {self.color} in color. It is {self.ripe} that it is ripe."

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'name': self.name,
        'ripe': self.ripe,
        'color': self.color
    }
