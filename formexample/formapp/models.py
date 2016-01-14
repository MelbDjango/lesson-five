from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    awesome = models.BooleanField()

    class Meta:
        verbose_name_plural = 'People'

    def __str__(self):
        return '{} ({})'.format(self.name, 'Totally Awesome' if self.awesome else 'Lame')
