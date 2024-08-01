from rest_framework import serializers

from apps.tours.models import Category, Country, Destination


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    destination_count = serializers.SerializerMethodField

    def get_destinations_count(self, obj):
        return obj.destinations_set_count
    class Meta:
        model = Country
        fields = '__all__'


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
