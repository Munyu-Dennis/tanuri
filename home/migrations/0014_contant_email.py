# Generated by Django 3.0 on 2020-09-05 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200905_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='contant',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
