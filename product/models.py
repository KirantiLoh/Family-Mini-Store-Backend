from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True, unique=False)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    netto = models.PositiveIntegerField()
    link = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"