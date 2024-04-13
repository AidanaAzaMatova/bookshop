from django.db import models

class Profiles(models.Model):
    column_name = models.CharField(max_length=100, editable=False)
    is_visible = models.BooleanField(default=True)

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    price = models.IntegerField(default=0)

