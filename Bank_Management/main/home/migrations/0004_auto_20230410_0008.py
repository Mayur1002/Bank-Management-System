# Generated by Django 3.0.2 on 2023-04-09 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('message', models.CharField(max_length=1024)),
            ],
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='Account_No',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]