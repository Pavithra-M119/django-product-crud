from django.db import models

# Create your models here.
class Product(models.Model):
    productNumber=models.IntegerField(unique=True)
    name=models.CharField(max_length=20)
    quantity=models.IntegerField()
    price=models.IntegerField()
    
