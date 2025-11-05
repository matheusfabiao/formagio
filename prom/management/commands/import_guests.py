import csv

from django.core.management.base import BaseCommand

from prom.models import PromGuest


class Command(BaseCommand):
    help = "Importa convidados do CSV para o banco"

    def handle(self, *args, **kwargs):
        with open('prom/data/prom_guests.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            imported = 0

            for row in reader:
                obj, created = PromGuest.objects.get_or_create(
                    first_name=row['first_name'],
                    last_name=row['last_name'] or None
                )
                if created:
                    imported += 1

        self.stdout.write(self.style.SUCCESS(f"{imported} convidados importados com sucesso!"))
