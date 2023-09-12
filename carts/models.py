from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from products.models import Product
from django.db.models.signals import pre_save, post_save


# Create your models here.
class Cart(models.Model):
    # objects = None
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)


class CartItems(models.Model):
    # objects = None

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    # total_items = models.IntegerField(default=0)
    quantity = models.IntegerField(default=1)


    #def __init__(self, *args, **kwargs):
        #super().__init__(args, kwargs)
       # self.product_name = None

    #def __str__(self):
       #return str(self.user.username) + " " + str(self.product_name)


@receiver(post_save, sender=CartItems)
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    # print(kwargs)
    price_of_product = Product.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
   # cart.total_price = cart_items.price
   # cart.save()
class Orders(models.Model):

   # total_cart_items=CartItems.objects.filter(user=cart_items.user)
    #cart_items.total_items = len(total_cart_items)

   # cart = Cart.objects.get(id=cart_items.cart.id)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    is_paid = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100,blank=True)
    payment_id = models.CharField(max_length=100,blank=True)
    payment_signature = models.CharField(max_length=100,blank=True)

class OrderedItems(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)



