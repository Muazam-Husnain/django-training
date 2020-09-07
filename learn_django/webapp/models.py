from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    company = models.CharField(max_length=100, default=None)
    address = models.TextField(default=None)

    def __str__(self):
        return self.name
