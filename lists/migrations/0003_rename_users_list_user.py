# Generated by Django 4.0.1 on 2022-06-01 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_list_rooms_alter_list_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='users',
            new_name='user',
        ),
    ]
