# Generated by Django 2.1 on 2019-01-10 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='CategoryName',
            new_name='categoryName',
        ),
    ]
