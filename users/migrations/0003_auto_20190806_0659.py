# Generated by Django 2.1.5 on 2019-08-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
        ('users', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gold_member',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='product_list',
            field=models.ManyToManyField(blank=True, related_name='product_lists', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='service_list',
            field=models.ManyToManyField(blank=True, related_name='service_lists', to='shop.Service'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='support_list',
            field=models.ManyToManyField(blank=True, related_name='support_lists', to='shop.Support'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(blank=True),
        ),
    ]
