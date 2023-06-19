from django.db import models
from .user_model import Client

class Book(models.Model):
    id_book = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=254)
    id_user = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.book_name}"
    
# Create your models here.
