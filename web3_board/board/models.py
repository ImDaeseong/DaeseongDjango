from django.db import models


class board_content(models.Model):
    sTitle = models.CharField(max_length=50, verbose_name='제목')
    sContent = models.TextField(verbose_name='내용')
    dCreated = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    dUpdated = models.DateTimeField(auto_now=True, verbose_name='수정일')
    iImage = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='이미지')
    objects = models.Manager()

    def __str__(self):
        return self.sTitle

    def summary(self):
        return self.sContent[:10] + str('...')

    class Meta:
        db_table = 'board_content'  # 테이블 이름
        verbose_name = '게시판 내용'
        verbose_name_plural = '게시판 내용'
