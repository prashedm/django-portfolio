from django.db import models

class news(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=25000)
    image = models.ImageField(upload_to='blog/images/', blank=True)
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title
