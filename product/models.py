from django.db import models

# Create your models here.
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.name
