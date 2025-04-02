from django.db import models

# Create your models here.

class Painting(models.Model):
    name = models.CharField(max_length=300)
    year = models.IntegerField(blank=True, null= True)
    description = models.TextField(blank=True, default="")
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    origin_nation = models.ForeignKey("OriginNation", on_delete=models.SET_NULL, null=True)
    art_movement = models.ForeignKey("ArtMovement", on_delete=models.SET_NULL, null=True)
    technique = models.ForeignKey("Technique", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Painting <{self.id}> {self.name}"
    
class Author(models.Model):
    name = models.CharField(max_length=300)
    birth_year = models.IntegerField(blank=True, null= True)
    death_year = models.IntegerField(blank=True, null= True)
    nationality = models.ForeignKey("Nationality", on_delete=models.SET_NULL, null=True)
    profession = models.CharField(max_length=300, default="")
    description = models.TextField(blank=True, default="")

    def __str__(self):
        return f"Author <{self.id}> {self.name}"
    
class OriginNation (models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Nation <{self.id}> {self.name}"
    
class ArtMovement (models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Art Movement <{self.id}> {self.name}"
    
class Technique (models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Techique <{self.id}> {self.name}"
    
class Nationality (models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"Nationality <{self.id}> {self.name}"
    
class MovementPainting (models.Model):
    movement = models.ForeignKey("ArtMovement", on_delete=models.SET_NULL, null=True)
    painting = models.ForeignKey("Painting", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"MovementPainting <{self.movement}> {self.painting}"
    
class PaintingTechnique (models.Model):
    technique = models.ForeignKey("Technique", on_delete=models.SET_NULL, null=True)
    painting = models.ForeignKey("Painting", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"TechniquePainting <{self.technique}> {self.painting}"
    
class AuthorNationality (models.Model):
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    nationality = models.ForeignKey("Nationality", on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"AuthorNationality <{self.author}> {self.nationality}"
