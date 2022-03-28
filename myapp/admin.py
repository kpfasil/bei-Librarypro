from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ["description", "image", "author", "book_name"][::-1]


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["profile_image","user"][::-1]


@admin.register(IssueBook)
class IssueBookAdmin(admin.ModelAdmin):
    list_display = ["issue_date", "book", "user"][::-1]
