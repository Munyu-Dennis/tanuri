# Generated by Django 3.0 on 2020-09-04 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20200905_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='myphoto',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]