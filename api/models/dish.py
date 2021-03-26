from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Dish(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  price = models.IntegerField()
  description = models.CharField(max_length=100)
  upload= models.ImageField(upload_to='uploads/', max_length=100)
  owner = models.ForeignKey(
      get_user_model(),
      related_name='dishes',
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"The dish named '{self.name}' is {self.price}. It is {self.description} that looks like this {self.upload}."

  def as_dict(self):
    """Returns dictionary version of Dish models"""
    return {
        'id': self.id,
        'name': self.name,
        'price': self.price,
        'description': self.discription,
        'photo': self.upload
    }
