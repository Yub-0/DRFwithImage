from django.db import models


class Image(models.Model):
    image = models.ImageField(blank=False, null=False)
    name = models.CharField(max_length=25, null=True)

    def __str__(self):
        return str(self.name)
