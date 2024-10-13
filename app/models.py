from django.db import models

# Create your models here.

class Trending(models.Model):
    from_social = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    likes_count = models.FloatField(null=True, blank=True)
    comments_count = models.FloatField(null=True, blank=True)
    views_count = models.FloatField(null=True, blank=True)
    input_text = models.CharField(max_length=244)
    author_meta = models.CharField(max_length=244)
    creation_date = models.CharField(max_length=244)

    def __str__(self):
        return self.input_text

    