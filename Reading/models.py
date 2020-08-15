from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def books(self):
        count = Book.objects.filter(category=self).count()
        return count

class Book(models.Model):
    name = models.CharField(max_length=500)
    author = models.ManyToManyField(Author, related_name='author')
    image = models.URLField(default='https://i.ibb.co/R4yFs3K/blank-book-cover-template-with-pages-front-side-standing-47649-397.jpg')
    summary = models.TextField(null=True, blank=True)
    rating = models.FloatField(default=0.0)
    category = models.ManyToManyField(Category, related_name='category')

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True, null=True)
    books = models.ManyToManyField(Book, through='Read')

    def __str__(self):
        return self.name


class Read(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    progress = models.CharField(max_length=10, default='0.00%', null=True, blank=True)
