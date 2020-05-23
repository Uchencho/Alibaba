from django.db import models
import random, os

def get_filename_ext(filepath):
    """
    Returns filename extension
    """
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    random_int = random.randint(1, 34908463)
    ext = get_filename_ext(filename)[1]
    new_filename = f'{random_int}{ext}'
    return f"products/{random_int}/{new_filename}"

class Product(models.Model):
    title           = models.CharField(max_length=50)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=9, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    def __str__(self):
        return self.title