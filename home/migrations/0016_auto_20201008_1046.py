# Generated by Django 3.0 on 2020-10-08 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20201008_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='myphoto',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
    ]
