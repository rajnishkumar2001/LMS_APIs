# Generated by Django 4.0.6 on 2022-07-15 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryApp', '0004_remove_register_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='last_login',
        ),
    ]
