# Generated by Django 2.1.5 on 2019-08-04 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecommendModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('residing_city', models.CharField(max_length=10)),
                ('residing_country', models.CharField(max_length=10)),
                ('total_purchase', models.DecimalField(decimal_places=2, max_digits=5)),
                ('total_cost', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
