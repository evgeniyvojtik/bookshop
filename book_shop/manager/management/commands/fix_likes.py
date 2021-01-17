from django.core.management import BaseCommand
from django.db.models import Count

from manager.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        book = Book.objects.annotate(count_like=Count('users_like'))
        print([(i.likes, i.count_like) for i in book])

        for b in book:
            b.likes = b.count_like
        Book.objects.bulk_update(book, ['likes'])
