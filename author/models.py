from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=20)

    def __str__(self):
        return self.first_name + self.last_name

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to=Author)

    def __str__(self):
        return self.title