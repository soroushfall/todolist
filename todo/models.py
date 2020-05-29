from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    priority = models.IntegerField(default=1)
    is_complete = models.BooleanField(default=False)

