from django.db import models

# Create your models here.

class Product(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
