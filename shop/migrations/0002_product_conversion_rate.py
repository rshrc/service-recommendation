# Generated by Django 2.1.5 on 2019-08-06 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='conversion_rate',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]