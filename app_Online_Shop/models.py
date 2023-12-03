from django.db import models

# Create your models here.

class Online_Shop(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255, verbose_name='Name')
    info = models.TextField()
    price = models.IntegerField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(

        'auth.User',
        on_delete=models.CASCADE,
        default = 1

    )
    body = models.TextField

    def __str__(self):
        return self.title