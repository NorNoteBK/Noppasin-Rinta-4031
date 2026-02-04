from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)

    def str(self):
        return f"{self.user_id} - {self.user_name}"

class Store(models.Model):
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    def str(self):
        return f"{self.store_id} - {self.store_location}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def str(self):
        return self.name