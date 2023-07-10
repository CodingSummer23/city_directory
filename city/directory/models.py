from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=30, unique=True, null=True)

    def __str__(self) -> str:
        return self.name
    

class Store(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=100, null=True)

    categories = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.name

