from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=32)
    email_id = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=64)
    phone_no = models.BigIntegerField()
    address = models.TextField()

    def __str__(self):
        return self.username + " - " + self.email_id


class Products(models.Model):
    product_name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product_name + "-" + str(self.price)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Products)
    total_amount = models.FloatField()
    status = models.BooleanField(default=False)  # False means order is not delivered yet. True means the order is delivered.
    status = models.BooleanField(default=False)  # False means order is not delivered yet. True means the order has been delivered.
    status = models.BooleanField(default=False)  # False means order is not placed yet
                                                # True means order has been placed and waiting for delivery
    date_ordered = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Order by ' + self.user.username + ' on ' + str(self.total_amount)