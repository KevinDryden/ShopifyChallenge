# Generated by Django 3.1.3 on 2021-05-09 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ArtWork', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='File',
            field=models.FileField(max_length=200, upload_to='../Media'),
        ),
    ]
