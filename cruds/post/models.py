from django.db import models

# Create your models here.

class Post(models.Model):
    header=models.CharField(max_length=120,verbose_name="header")
    text=models.TextField(verbose_name="text")
    create_date=models.DateTimeField(verbose_name="date",auto_now_add=True)


    def  __str__(self):
        return self.header