# Generated by Django 3.1.7 on 2023-03-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0002_cours_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='cours-thumbnails/'),
        ),
    ]
