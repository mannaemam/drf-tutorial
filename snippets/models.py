from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

import uuid
from django.utils.text import slugify

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default='python', max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            title_slug = slugify(self.title) or 'snippet'
            self.slug = f'{title_slug}-{self.id}'

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['created']