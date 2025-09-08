from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    img = models.ImageField(upload_to="product", height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name