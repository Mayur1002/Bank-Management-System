# Generated by Django 3.0.2 on 2023-04-02 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Account_No', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('Balance', models.IntegerField()),
                ('Username', models.CharField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
