from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    def __str__(self):
        return self.title

class feed(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description = models.TextField(max_length=3000)
    url = models.URLField(blank=True)
#    def __str__(self):
#        return self.title
