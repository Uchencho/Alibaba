from django.db import models

class Product(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=9, default=39.99)

    def __str__(self):
        return self.title