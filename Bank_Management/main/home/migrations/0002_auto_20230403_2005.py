# Generated by Django 3.0.2 on 2023-04-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.CharField(default='', max_length=50),
        ),
    ]