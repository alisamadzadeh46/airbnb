from django.core.management.base import BaseCommand
from rooms.models import Amenity


class Command(BaseCommand):
    help = "This command create amenities"

    def handle(self, *args, **options):
        amenities = [
            "Air conditioning",
            "Alarm clock",
            "Balcony",
            "Bathroom"
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))
