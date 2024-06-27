from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='customer')
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    contact_number = models.IntegerField()

    def __str__(self):
        return self.name

class Productz(models.Model):
    pname = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/')
    description = models.TextField()

    def __str__(self):
        return self.pname

class CartItem(models.Model):
    productz = models.ForeignKey(Productz, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.productz.pname}'
