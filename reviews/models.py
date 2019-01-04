from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug  = models.SlugField()
    summary  = models.TextField()
    key_words = models.TextField()
    body_html = models.TextField()
    date  = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.summary[:200] + '...'