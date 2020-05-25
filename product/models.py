from django.db import models
import random, os
from django.urls import reverse

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
    return f"products/{random_int}/{new_filename}" #Better to use f"products/{new_filename}"

class ProductQuerySet(models.query.QuerySet):
    #Creating a custom queryset
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        # Overwriting the custom queryset
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        # This is so that whenever you call the .all(), it returns only active products
        # You could decide to only use .active() the way we use .featured()
        return self.get_queryset().active()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Products.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def get_by_slug(self, slug):
        qs = self.get_queryset().filter(slug=slug) # Products.objects == self.get_queryset()
        if qs.count() == 0:
            return None
        return qs.first()

    def featured(self):
        return self.get_queryset().filter(featured=True)

class Product(models.Model):
    title           = models.CharField(max_length=50)
    slug            = models.SlugField(default='abc', unique=True)
    description     = models.TextField()
    price           = models.DecimalField(decimal_places=2, max_digits=9, default=39.99)
    image           = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    featured        = models.BooleanField(default=False)
    active          = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        """
        Returns the absolute url for a specific object
        """
        return reverse("product:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title