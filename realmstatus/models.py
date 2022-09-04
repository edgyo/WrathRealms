from django.db import models

# Create your models here.

class Realm(models.Model):
    name = models.CharField(max_length=20)
    is_up = models.BooleanField()
    status = models.CharField(max_length=40)

    def __str__(self):
        return self.name