from django.db import models

# Create your models here.

class retreats(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='retreats/images/')
    price = models.IntegerField()
    duration = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title