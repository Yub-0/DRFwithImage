from django.db import models


class Product(models.Model):
    p_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=25)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(blank=False, null=False)

    def __str__(self):
        return self.product.name
