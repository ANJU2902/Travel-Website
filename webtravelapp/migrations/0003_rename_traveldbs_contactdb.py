# Generated by Django 3.2.6 on 2022-02-24 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtravelapp', '0002_rename_traveldb_traveldbs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='traveldbs',
            new_name='contactdb',
        ),
    ]
