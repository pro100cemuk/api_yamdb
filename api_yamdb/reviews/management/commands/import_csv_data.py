import csv
import os

from django.core.management.base import BaseCommand, CommandError

from api_yamdb.settings import BASE_DIR
from reviews.models import Comments, Reviews, Titles, User


class Command(BaseCommand):
    help = 'Import initial data from file static/data/*.csv args sequensial'

    def add_arguments(self, parser):
        parser.add_argument('files', nargs='+', type=str)

    def handle(self, *args, **options):
        obj = {
            'users.csv': User,
            'category.csv': object(),
            'genre.csv': object(),
            'titles.csv': Titles,
            'genre_title.csv': object(),
            'review.csv': Reviews,
            'comments.csv': Comments
        }
        dir_data = os.path.join(BASE_DIR, "static/data")
        for file_csv in options['files']:
            if file_csv not in obj.keys():
                raise CommandError('Unknown file to import "%s"' % file_csv)
            try:
                full_fn = os.path.join(dir_data, file_csv)
                print(full_fn)
                with open(full_fn, 'r', newline='', encoding='utf-8') as csvf:
                    reader = csv.DictReader(csvf)
                    list_obj = list(
                        obj[file_csv](**kwargs)
                        for kwargs in reader
                    )
                    obj[file_csv].objects.bulk_create(list_obj)
            except OSError:
                raise CommandError('File "%s" does not exist' % file_csv)
            self.stdout.write(
                self.style.SUCCESS('Successfully files "%s"' % file_csv)
            )
