# Generated by Django 3.1.5 on 2022-05-26 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0003_auto_20220526_1951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.AddField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(blank=True, related_name='categories', to='blogging.Post'),
        ),
    ]
