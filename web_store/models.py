from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    details = models.TextField() 
    photo_1_url = models.TextField()
    photo_2_url = models.TextField()

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart', related_query_name='cart')
    quantity = models.IntegerField()

class CartItem(models.Model):
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart', related_query_name='cart')
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items', related_query_name='item')
    quantity = models.IntegerField()

class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.CharField(max_length=500)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', related_query_name='comment')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title