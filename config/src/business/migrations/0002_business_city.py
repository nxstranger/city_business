# Generated by Django 3.1.5 on 2021-01-24 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('business', '0001_initial'),
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_city', to='city.city'),
        ),
    ]
