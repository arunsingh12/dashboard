# Generated by Django 4.0.4 on 2022-06-01 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0010_alter_order_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_discription',
            field=models.CharField(max_length=100),
        ),
    ]
