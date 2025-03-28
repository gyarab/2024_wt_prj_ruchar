from django.contrib import admin
from .models import Painting, Author, OriginNation, ArtMovement, Technique, Nationality

class PaintingAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "year", "author", "origin_nation", "art_movement", "technique", "description"]

class AuthorAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "birth_year", "death_year", "nationality", "profession", "description"]

class OriginNationAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ArtMovementAdmin(admin.ModelAdmin):
    list_display = ["name"]

class TechniqueAdmin(admin.ModelAdmin):
    list_display = ["name"]

class NationalityAdmin(admin.ModelAdmin):
    list_display = ["name"]

# Register your models here.
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(OriginNation, OriginNationAdmin)
admin.site.register(ArtMovement, ArtMovementAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Nationality, NationalityAdmin)