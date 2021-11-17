from django.db import models
from django.db.models.fields import CharField, DateField

# Create your models here.
class Lost(models.Model):
    date = DateField()
    title = CharField(max_length=200)
    details = models.TextField()