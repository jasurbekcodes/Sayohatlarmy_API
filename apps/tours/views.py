from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.tours.models import Category, Country, Destination
from apps.tours.serializers import CategorySerializer, CountrySerializer, DestinationSerializer


@api_view(['GET'])
def featured_categories_view(request):
    categories = Category.objects.all()[:5]
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, 200)

@api_view(['GET'])
def featured_countries_view(request):
    countries = Country.objects.all()[:3]
    serializer = CountrySerializer(countries, many=True)
    return Response(serializer.data, 200)


@api_view(['GET'])
def featured_destinations_view(request):
    countries = Destination.objects.all()[:10]
    serializer = DestinationSerializer(countries, many=True)
    return Response(serializer.data, 200)
