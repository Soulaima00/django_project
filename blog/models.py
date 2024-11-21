from django.conf import settings
from django.db import models
from django.utils import timezone


class Reclamation(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField("Titre de la réclamation", max_length=200)
    text = models.TextField("Texte de la réclamation")
    created_date = models.DateTimeField("Date de création", default=timezone.now)
    published_date = models.DateTimeField("Date de publication", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} par {self.author}"
