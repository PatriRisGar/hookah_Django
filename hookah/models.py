from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class HookahTobacco(models.Model):
    STATUS = (
        ('blond', 'Rubio'),
        ('dark', 'Negro')
    )

    image = models.ImageField(upload_to='hookahTobacco_images/', null=True, blank=True)
    name = models.CharField(max_length=25)
    brand = models.CharField(max_length=25)
    type = models.CharField(max_length=20,choices=STATUS)
    description = models.TextField()    
    averageRating = models.FloatField(default=0)
    ratingCount = models.PositiveIntegerField(default=0)
    registeredDay = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('name', 'brand')

    def __str__(self):
        return f"{self.name} de {self.brand}"