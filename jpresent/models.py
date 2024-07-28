from django.db import models
from django.utils import timezone

class Presentation(models.Model):
    date = models.DateField(default=timezone.now, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    pdf_url_link = models.URLField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdf_files/', blank=True, null=True)
    tag = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else 'Untitled'

