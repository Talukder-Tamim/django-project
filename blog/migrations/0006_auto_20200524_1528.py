# Generated by Django 2.1.7 on 2020-05-24 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='author',
            new_name='user',
        ),
    ]