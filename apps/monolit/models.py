from colorfield.fields import ColorField
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200, unique_for_date='date')
    title_color = ColorField(default=0xffffff)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    images = models.ImageField(null=True)

    def __str__(self):
        return f'{self.title}-{self.date}'
