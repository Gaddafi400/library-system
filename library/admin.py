from django.contrib import admin
from django.utils.html import format_html
from .models import User, UserProfile, Book, Author, BookOutLoan, Fine, Genre, Publisher, ContactUs


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['book_title', 'ISBN', 'genre', 'date', 'thumbnail']
    list_per_page = 8
    
    def thumbnail(self, instance):
        if instance.cover_page != '':
            return format_html(f'<img src="{instance.cover_page.url}" style="width:100px; height:100px; object-fit: cover; border-radius: 5%" class="thumbnail" />') 
        return ''


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(BookOutLoan)
class BookOutLoanAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'date_issue', 'date_due_for_return']

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'date_of_birth', 'profile_pic']
    
    def profile_pic(self, instance):
        if instance.profile_photo != '':
            return format_html(f'<img src="{instance.profile_photo.url}" style="width:100px; height:100px; object-fit: cover; border-radius: 5%"/>') 
        return ''

@admin.register(User)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email']
    
 
admin.site.register(Publisher)
admin.site.register(Fine)
admin.site.register(Genre)
admin.site.register(ContactUs)
