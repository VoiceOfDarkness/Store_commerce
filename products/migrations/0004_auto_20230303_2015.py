# Generated by Django 3.2.18 on 2023-03-03 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RenameField(
            model_name='basket',
            old_name='Product',
            new_name='product',
        ),
    ]
