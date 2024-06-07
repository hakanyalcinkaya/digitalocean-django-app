from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='products/')

    def __str__(self):
        return self.title

