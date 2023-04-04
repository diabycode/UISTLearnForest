import json
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.core import serializers

from cours.models import Cours, Section, Video, Article


class Command(BaseCommand):
    help = 'Get all datas from the database'

    def add_arguments(self, parser):
        parser.add_argument('--output', type=str, default='datas.json')

    def handle(self, *args, **options):
        output_filename = options.get('output')

        # create output file with Path
        output_file = Path().cwd() / output_filename
        if not output_file.exists():
            output_file.touch()
        

        # get courses and serialize them
        courses = json.loads(serializers.serialize('json', Cours.objects.all().order_by('create_at')))

        # get sections and serialize them
        sections = json.loads(serializers.serialize('json', Section.objects.all().order_by('create_at')))

        # get videos and serialize them
        videos = json.loads(serializers.serialize('json', Video.objects.all().order_by('create_at')))

        # get articles and serialize them
        articles = json.loads(serializers.serialize('json', Article.objects.all().order_by('create_at')))


        # final datas
        datas = {
            'courses': courses,
            'sections': sections,
            'videos': videos,
            'articles': articles,
        }

        # whrite all datas in the output file
        with open(output_file, 'w') as f:
            json.dump(datas, f, indent=4)

        self.stdout.write(self.style.SUCCESS(f'Output file: {output_file}'))

