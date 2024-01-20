from django.db import models

class Zikr(models.Model):
    category = models.CharField(max_length=50)
    text = models.TextField()
    meaning = models.TextField()
    count = models.IntegerField()