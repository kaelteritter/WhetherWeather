from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    lat = models.DecimalField(
        decimal_places=4,
        max_digits=7,
        blank=True, 
        null=True
        )
    lon = models.DecimalField(
        decimal_places=4,
        max_digits=7,
        blank=True, 
        null=True
        )
    
    def __str__(self):
        return self.name