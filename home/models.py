import uuid
from django.db import models


# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = [
        ('EC', 'Electronics'),
        ('CL', 'Clothing'),
        ('BK', 'Books'),
        # Add more choices as needed
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    price = models.FloatField(default=0.0)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='EC')
    in_stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
