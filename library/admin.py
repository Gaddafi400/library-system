from django.contrib import admin
from django.utils.html import format_html
from .models import User, UserProfile, Book, Author, BookOutLoan, Fine, Genre, Publisher, ContactUs


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'ISBN', 'thumbnail']
    
    def thumbnail(self, instance):
        if instance.cover_page.name != '':
            return format_html(f'<img src="{instance.cover_page.url}" style="width:100px; height:100px; object-fit: cover; border-radius: 5%" class="thumbnail" />') 
        return ''


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']



admin.site.register(Publisher)
admin.site.register(BookOutLoan)
admin.site.register(Fine)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(ContactUs)
