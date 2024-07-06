from django.db import models

# Create your models here.
class LibraryBook(models.Model):
    title = models.CharField(max_length = 60)
    author = models.CharField(max_length = 60)
    isbn = models.CharField(max_length = 60, unique=True)
    available = models.BooleanField()

    class Meta:
        ordering = ['author']
        indexes = [models.Index(fields=['isbn'])]