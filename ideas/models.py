import uuid
from django.db import models

# Create your models here.

class Idea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.CharField(max_length=25, default='')
    text = models.TextField()
    likes = models.IntegerField(default=0, editable=False)
