from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=200)
    contact = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order for {self.product.name} by {self.name}'