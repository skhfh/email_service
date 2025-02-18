# coding=utf-8
import csv
import datetime
import os

from django.core.management.base import BaseCommand

from newsletters.models import Subscriber
from newsletterservice.settings import BASE_DIR

csv_file = 'subscribers.csv'
csv_file_path = os.path.join(BASE_DIR, 'static', 'data', csv_file)


class Command(BaseCommand):
    help = 'Импорт подписчиков из CSV-файла в базу данных'

    def handle(self, *args, **options):
        with open(csv_file_path, 'rb') as f:
            try:
                rows = csv.DictReader(f)
                records = []
                for row in rows:
                    email = row['email'].decode('utf-8')
                    first_name = row['first_name'].decode('utf-8')
                    last_name = row['last_name'].decode('utf-8')
                    birth_date = datetime.datetime.strptime(row['birth_date'],
                                                            '%Y-%m-%d').date()
                    records.append(Subscriber(
                        email=email,
                        first_name=first_name,
                        last_name=last_name,
                        birth_date=birth_date
                    ))
                Subscriber.objects.bulk_create(records)
                self.stdout.write(self.style.SUCCESS('Done'))
            except Exception as error:
                self.stdout.write(self.style.ERROR('ERROR %s' % error))
