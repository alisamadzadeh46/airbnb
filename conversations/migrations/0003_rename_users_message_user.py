# Generated by Django 4.0.1 on 2022-06-01 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0002_alter_conversation_participants_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='users',
            new_name='user',
        ),
    ]
