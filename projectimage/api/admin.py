from django.contrib import admin

# Register your models here.
from api.models import Product, Image

admin.site.register(Product)
admin.site.register(Image)
