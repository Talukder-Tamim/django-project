# Generated by Django 2.1.7 on 2020-05-20 08:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='post',
        ),
    ]