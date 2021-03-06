# Generated by Django 3.1.5 on 2021-01-24 09:50

from django.db import migrations, models
import src.business.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, unique=True)),
                ('price_multiplier', models.PositiveIntegerField(validators=[src.business.models.multiplier_validator])),
            ],
        ),
    ]
