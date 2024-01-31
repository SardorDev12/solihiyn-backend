from django.conf import settings
from django.db import models


class Zikr(models.Model):
    category = models.CharField(max_length=50)
    text = models.TextField()
    meaning = models.TextField()
    count = models.IntegerField()
    count_val = models.IntegerField(default=0)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.category} - {self.text}"
