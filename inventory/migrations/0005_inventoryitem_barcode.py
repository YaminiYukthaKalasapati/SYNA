# Generated by Django 5.1.2 on 2024-11-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_inventoryitem_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryitem',
            name='barcode',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
