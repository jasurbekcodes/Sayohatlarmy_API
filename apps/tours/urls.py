from django.urls import path

from apps.tours.views import featured_categories_view, featured_countries_view, featured_destinations_view


urlpatterns = [
    path('featured-categories/', featured_categories_view, name='featured_categories'),
    path('featured-countries/', featured_countries_view, name='featured_countries'),
    path('featured-destinations/', featured_destinations_view, name='featured_destinations'),
]

