# Generated by Django 3.1.1 on 2020-09-17 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='username',
            new_name='user',
        ),
    ]
