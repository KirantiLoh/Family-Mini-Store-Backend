from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = CloudinaryField('image')
    name = models.CharField(max_length=100)
    netto = models.PositiveIntegerField()
    link = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"