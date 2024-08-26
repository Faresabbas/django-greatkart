from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_description = models.TextField(max_length=500)
    product_slug = models.SlugField(max_length=100, unique=True)
    product_stock = models.IntegerField()
    image = models.ImageField(upload_to='photos/products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    date_uploaded = models.DateTimeField(auto_now=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_absolute_url(self):
        return reverse('product_detail', args=[self.category.slug, self.product_slug])
    def __str__(self):
        return self.product_name
