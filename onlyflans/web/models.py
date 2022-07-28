from email.mime import message
from django.db import models
import uuid

# Create your models here.

class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=64)
    description = models.TextField(null=True)
    image_url = models.URLField(null=True)
    slug = models.SlugField(null=True)
    price = models.FloatField(default=6000)
    is_private = models.BooleanField(null=True)
    
    
    def __str__(self):
        return f'{self.flan_uuid} {self.name} {self.description} {self.image_url} {self.price} {self.is_private}'
    

class Contactform(models.Model):
    contact_form_uuid = models.UUIDField(default=uuid.uuid4,editable=False)
    customer_email = models.EmailField(null=True)
    customer_name = models.CharField(max_length=64)
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=1000)
    
def __str__(self):
    return f'{self.contact_form_uuid} {self.customer_name} {self.customer_email} {self.subject} {self.message}'

"""
class Recetas(models.Model):
    recipe_uuid = models.UUIDField(default=uuid.uuid4)
    recipe_name = models.CharField(max_length=64)
    ingredients = models.TextField(null=True) 
    preparation = models.TextField(null=True)
    
    def __str__(self):
        return f'{self.recipe_uuid} {self.recipe_name} {self.ingredients} {self.preparation}'
"""    