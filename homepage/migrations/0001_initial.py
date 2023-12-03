# Generated by Django 4.2.6 on 2023-11-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100, verbose_name='Brand')),
                ('image', models.ImageField(upload_to='images/')),
                ('info', models.TextField()),
                ('price', models.IntegerField()),
            ],
            options={
                'db_table': 'home pages',
                'ordering': ['price'],
            },
        ),
    ]