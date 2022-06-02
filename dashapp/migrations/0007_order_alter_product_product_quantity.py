# Generated by Django 4.0.4 on 2022-05-31 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashapp', '0006_alter_category_id_alter_employee_id_alter_product_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=40)),
                ('price', models.IntegerField()),
                ('created_time', models.DateTimeField(db_index=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(),
        ),
    ]