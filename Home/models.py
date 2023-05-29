from django.db import models

# Create your models here.
# Project Model.
class Project(models.Model):
    thumbnail = models.ImageField(upload_to='projects/')
    name = models.CharField(max_length=45)
    description = models.TextField(blank=False)
    test = models.TextField(blank=True)
