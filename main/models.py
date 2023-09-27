from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    date_added = models.DateField(auto_now_add=True)
    price = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    amount = models.IntegerField(
        validators=[MinValueValidator(0)]
    )
    description = models.TextField()

    #method untuk tambah jumlah stok produk sebanyak satu item
    def add_product(self, quantity):
        self.amount += quantity
        self.save()
    #method untuk mengurangi jumlah stok produk sebanyak satu item
    def subtract_product(self, quantity):
        if self.amount >= quantity:
            self.amount -= quantity
            self.save()

    def __str__(self):
        return self.name