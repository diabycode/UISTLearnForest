# Generated by Django 3.1.7 on 2023-03-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0003_cours_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='video_source',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
