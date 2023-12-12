from django.db import models

# Create your models here.
class MyFile(models.Model):
    title = models.CharField(max_length=20)
    arq = models.FileField(upload_to="img")
    # /media/img -> sempre será salvo na pasta media em diante

    def __str__(self) -> str:
        return self.title