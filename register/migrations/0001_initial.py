# Generated by Django 3.2.8 on 2021-10-27 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=240, verbose_name='First_name')),
                ('lname', models.CharField(max_length=240, verbose_name='Last_name')),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=240, verbose_name='address')),
                ('username', models.CharField(max_length=240, verbose_name='username')),
                ('password', models.CharField(max_length=240, verbose_name='password')),
            ],
        ),
    ]
