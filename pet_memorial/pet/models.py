from django.db import models
from django.utils.text import slugify

class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    slug = models.SlugField(allow_unicode=True, max_length=100, unique=True, default="default_pet_slug")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("pet:pet_details", kwargs={"slug": self.slug})
