from django.contrib import admin
from .models import Painting, Author

class PaintingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "author", "description"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "description"]

# Register your models here.
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Author, AuthorAdmin)