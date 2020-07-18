from django.contrib import admin

from book.models import Book, Author, CopyOfBook

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(CopyOfBook)


