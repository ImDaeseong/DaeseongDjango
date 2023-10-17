# Generated by Django 4.2.6 on 2023-10-17 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('pwd', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('sTitle', models.CharField(max_length=50)),
                ('sContent', models.CharField(max_length=4000)),
                ('dCreated', models.DateTimeField(null=True)),
                ('readcnt', models.IntegerField(default=0)),
                ('filename', models.CharField(max_length=300)),
            ],
        ),
    ]
