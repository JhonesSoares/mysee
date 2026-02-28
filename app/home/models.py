from django.db import models
from utils.image_size import imageSize


class Services(models.Model):
    title = models.CharField(max_length=65)
    cover = models.ImageField(upload_to="home/covers/%Y/%m/%d/", blank=True, default="")
    image = imageSize()
    text = models.TextField(max_length=600, blank=True, null=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover:
            self.image.resize_image(self.cover, 800)

    def __str__(self):
        return self.title


class About(models.Model):
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to="home/covers/%Y/%m/%d/", blank=True, default="")
    image = imageSize()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.cover:
            self.image.resize_image(self.cover, 800)

    def __str__(self):
        return self.name
