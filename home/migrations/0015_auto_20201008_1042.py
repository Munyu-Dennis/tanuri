# Generated by Django 3.0 on 2020-10-08 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_contant_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='myphoto',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
