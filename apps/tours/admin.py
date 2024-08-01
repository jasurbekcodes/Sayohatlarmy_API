from django.contrib import admin
from apps.tours.models import Category, Country, Destination


admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Destination)

