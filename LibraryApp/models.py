from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class AppUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin','Admin'),
        ('librarian','Librarian'),
        ('member','Member')
    ]

    role = models.CharField(max_length=100,choices=ROLE_CHOICES)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    added_by = models.ForeignKey(AppUser,on_delete=models.CASCADE,related_name='books')

class Borrow(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrower = models.ForeignKey(AppUser,on_delete=models.CASCADE,related_name='borrow_history')
    borrowed_on = models.DateField(auto_now_add=True)
