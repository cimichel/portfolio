from django.db import models


class MemeTrivia(models.Model):
    title = models.CharField(max_length=100)
    options = models.TextField()
    image = models.FileField(upload_to="memetrivia_img/", blank=True)
