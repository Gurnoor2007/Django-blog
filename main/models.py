from django.db import models

# Create your models here.

class Contact (models.Model):
    contact_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=40)
    topic = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)