from django.db import models

class Schedule(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)