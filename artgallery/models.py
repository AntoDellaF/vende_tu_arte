from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ArtPiece(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='art_pieces/')

    def __str__(self):
        return self.title