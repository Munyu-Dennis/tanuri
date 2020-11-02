# Generated by Django 3.0 on 2020-10-16 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20201008_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oder',
            name='name',
            field=models.CharField(default='none', max_length=150),
        ),
        migrations.AlterField(
            model_name='oder',
            name='phone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='OrderIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Table_Number', models.IntegerField(default=0)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Menu')),
            ],
        ),
    ]