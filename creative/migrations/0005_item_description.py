# Generated by Django 3.1.3 on 2020-12-03 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creative', '0004_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='this is the testting purpose'),
            preserve_default=False,
        ),
    ]
