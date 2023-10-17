from django.db import models


# Create your models here.
# python manage.py makemigrations
# python manage.py migrate


class Board(models.Model):
    number = models.AutoField(primary_key=True)
    pwd = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    sTitle = models.CharField(max_length=50)
    sContent = models.CharField(max_length=4000)
    dCreated = models.DateTimeField(null=True)  # null 허용
    readcnt = models.IntegerField(default=0)
    filename = models.CharField(max_length=300)

    def __str__(self):
        return str(self.number) + ":" + self.sTitle
