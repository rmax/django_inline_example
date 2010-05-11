from django.contrib import admin
from books.models import Author, Book

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
    max_num = 10

class AuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
