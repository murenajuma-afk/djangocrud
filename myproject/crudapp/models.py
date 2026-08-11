from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='product/')
    created_at = models.DateTimeField(auto_now_add=True)
 

    def __str__(self):
        return f'Product name: {self.name} Price: {self.price} image: {self.image} created_at: {self.created_at}'
