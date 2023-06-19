from django.db import models


class Client(models.Model):
    id_user = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=254)
    user_email = models.EmailField(max_length=254)
    def __str__(self):
        return f"{self.user_name}"
# Create your models here.
