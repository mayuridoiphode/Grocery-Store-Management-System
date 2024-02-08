from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,blank=True)
    #@property
    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
    #@property
    def __str__(self):
        return str(self.category_name)


class QuantityVariant(models.Model):
    variant_name = models.CharField(max_length=100)

    #@property
    def __str__(self):
        return str(self.variant_name)


class ColorVariant(models.Model):
    color_name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

   # @property
    def __str__(self):
        return str(self.color_name)


class SizeVariant(models.Model):
    size_name = models.CharField(max_length=100)
   # @property
    def __str__(self):
        return str(self.size_name)





class Product(models.Model):
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products',default='default.jpg')
    price = models.CharField(max_length=20)
    description = models.TextField()
    stock = models.IntegerField(default=100)


    quantity_type = models.ForeignKey(QuantityVariant, blank=True, null=True, on_delete=models.PROTECT)
    color_type = models.ForeignKey(ColorVariant, blank=True, null=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(SizeVariant, blank=True, null=True, on_delete=models.PROTECT)

    #@property
    def __str__(self):
        return str(self.product_name)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/products',default='default.jpg')

    