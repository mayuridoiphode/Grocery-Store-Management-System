# Generated by Django 2.2.7 on 2023-09-08 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20230908_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='static/products'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='product_name',
            field=models.ForeignKey(default=100, on_delete=django.db.models.deletion.PROTECT, to='products.Product'),
        ),
    ]
