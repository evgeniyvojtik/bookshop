from django.core.management import BaseCommand
from django.db.models import Count, Sum
from manager.models import Book


class Command(BaseCommand):
    def handle(self, *args, **options):
        books = Book.objects.annotate(
            tmp_all_stars=Sum('users_rate__rate'),
            tmp_rated_users=Count('users_rate')
        )
        for b in books:
            b.users_counted_stars = b.tmp_all_stars
            b.count_users = b.tmp_rated_users
            b.rate = b.tmp_all_stars / b.tmp_rated_users
            Book.objects.bulk_update(books, ['users_counted_stars', 'count_users', 'rate'])


