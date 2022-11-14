from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


import string
from django.utils.text import slugify
import random

def random_string_generator(size = 10, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug = None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.first_name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug = slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug = slug, randstr = random_string_generator(size = 4))

        return unique_slug_generator(instance, new_slug = new_slug)
    return slug


from django.db.models.signals import pre_save

def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)

pre_save.connect(pre_save_receiver, sender = Pet)
