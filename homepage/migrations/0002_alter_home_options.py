# Generated by Django 4.2.6 on 2023-11-02 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'ordering': ['brand']},
        ),
    ]
