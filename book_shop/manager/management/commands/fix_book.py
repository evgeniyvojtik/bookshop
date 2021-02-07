from django.core.management import BaseCommand

from manager.models import TMPBook, Book, UsersRating


class Command(BaseCommand):
    def handle(self, *args, **options):
        arr = [TMPBook(
            title=b.title,
            date=b.date,
            description=b.description,
            rate=b.rate,
            slug=b.slug,
            users_counted_stars=b.users_counted_stars,
            count_users=b.count_users
        )
            for b in Book.objects.all()]
        TMPBook.objects.bulk_create(arr)
        query = Book.objects.all().values("slug", 'id')
        ur = UsersRating.objects.all()
        for book in query:
            new_set = ur.filter(book_id=book['id'])
            for i in new_set:
                i.tmp_book_id = book['slug']
                i.save()

