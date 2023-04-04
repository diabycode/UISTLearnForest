import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers

from cours.models import Cours, Section, Video, Article
from base import settings
from accounts.models import UserModel

class Command(BaseCommand):
    help = 'Create datas in database'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        filename = options.get('filename')
        filepath = settings.BASE_DIR / filename

        # get datas from json file
        with open(str(filepath.resolve()), 'r') as f:
            datas = json.load(f)


        # create Courses
        for cours in datas.get('courses'):
            c = Cours.objects.create(
                pk=cours['pk'],
                title=cours['fields'].get('title'),
                description=cours['fields'].get('description'),
                create_at=cours['fields'].get('create_at'),
                thumbnail=cours['fields'].get('thumbnail'),
                slug=cours['fields'].get('slug'),
            )        
            try:
                c.author = UserModel.objects.get(pk=cours['fields'].get('author'))
            except UserModel.DoesNotExist:
                c.author = None

            c.save()


        # create Sections
        for section in datas.get('sections'):
            Section.objects.create(
                pk=section['pk'],
                title=section['fields'].get('title'),
                create_at=section['fields'].get('create_at'),
                cours=Cours.objects.get(pk=section['fields'].get('cours')),
            )
        
        # create Videos
        for video in datas.get('videos'):
            Video.objects.create(
                pk=video['pk'],
                title=video['fields'].get('title'),
                create_at=video['fields'].get('create_at'),
                section=Section.objects.get(pk=video['fields'].get('section')),
                video_source=video['fields'].get('video_source'),
                description=video['fields'].get('description'),
            )

        # create Articles
        for article in datas.get('articles'):
            Article.objects.create(
                pk=article['pk'],
                title=article['fields'].get('title'),
                create_at=article['fields'].get('create_at'),
                section=Section.objects.get(pk=article['fields'].get('section')),
                content=article['fields'].get('content'),
            )

        self.stdout.write(self.style.SUCCESS('Datas created successfully'))

    