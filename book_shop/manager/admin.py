from django.contrib import admin
from manager.models import Book, Comment


class CommentAdmin(admin.StackedInline):
    model = Comment
    extra = 2


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentAdmin]
    readonly_fields = ['rate']
    exclude = ['users_counted_stars', 'count_users']
    prepopulated_fields = {"slug": ('title',)}

admin.site.register(Book, BookAdmin)
