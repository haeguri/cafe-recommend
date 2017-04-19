from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    create_date = models.DateTimeField(auto_created=True, auto_now=True)