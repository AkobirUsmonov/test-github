from django.db import models

class Home(models.Model):
    nomi = models.CharField(max_length=100, verbose_name='Brand')
    image = models.ImageField(upload_to='images/')
    info = models.TextField()
    price = models.IntegerField()

    class Meta:
        db_table = 'home pages'
        ordering = ['nomi']


class Info(models.Model):
    nomi = models.CharField(max_length=100, verbose_name='Brand')
    image = models.ImageField(upload_to='images/')
    info = models.TextField()
    price = models.IntegerField()
    author = models.CharField(max_length=200, verbose_name='mualif')

    class Meta:
        db_table = 'info'
        ordering = ['nomi']


class About_Us(models.Model):
    nomi = models.CharField(max_length=100, verbose_name='Brand')
    image = models.ImageField(upload_to='images/')
    info = models.TextField()

    class Meta:
        db_table = 'about us'
        ordering = ['nomi']

class Online_books(models.Model):
    nomi = models.CharField(max_length=100, verbose_name='Brand')
    image = models.ImageField(upload_to='images/')
    info = models.TextField()
    pdf = models.TextField(max_length=200, verbose_name='pdf')

    class Meta:
        db_table = 'online_books'
        ordering = ['nomi']