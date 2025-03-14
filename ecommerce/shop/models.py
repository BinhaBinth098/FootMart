from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.TextField()
    image=models.ImageField(upload_to="images")
    def __str__ (self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=50)

    desc=models.TextField()
    image=models.ImageField(upload_to="products")
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name