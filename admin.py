from django.contrib import admin
from .models import PythonType, Product, Review

# Register your models here.
admin.site.register(PythonType)
admin.site.register(Product)
admin.site.register(Review)