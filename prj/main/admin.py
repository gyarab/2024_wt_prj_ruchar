from django.contrib import admin
from .models import Painting, Author, OriginNation, ArtMovement, Technique, Nationality, MovementPainting, PaintingTechnique, AuthorNationality

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
    
class MovementPaintingAdmin(admin.ModelAdmin):
    list_display = ["movement", "painting"]
    
class PaintingTechniqueAdmin(admin.ModelAdmin):
    list_display = ["technique", "painting"]
    
class AuthorNationalityAdmin(admin.ModelAdmin):
    list_display = ["author", "nationality"]    
    
# Register your models here.
admin.site.register(Painting, PaintingAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(OriginNation, OriginNationAdmin)
admin.site.register(ArtMovement, ArtMovementAdmin)
admin.site.register(Technique, TechniqueAdmin)
admin.site.register(Nationality, NationalityAdmin)
admin.site.register(MovementPainting, MovementPaintingAdmin)
admin.site.register(PaintingTechnique, PaintingTechniqueAdmin)
admin.site.register(AuthorNationality, AuthorNationalityAdmin)