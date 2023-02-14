from django.db import models

class BmiModel(models.Model):
    user = models.CharField(max_length=20)
    age = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
