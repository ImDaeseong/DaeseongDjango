from django.db import models


class board_content(models.Model):
    sTitle = models.CharField(max_length=50)
    sContent = models.TextField()
    dCreated = models.DateTimeField(auto_now_add=True)
    dUpdated = models.DateTimeField(auto_now_add=True)
    iImage = models.ImageField(upload_to='images', blank=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.sTitle
