# Generated by Django 4.1.1 on 2022-10-01 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_content_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='board_content',
            options={'ordering': ['dCreated'], 'verbose_name': '게시판 내용', 'verbose_name_plural': '게시판 내용'},
        ),
    ]