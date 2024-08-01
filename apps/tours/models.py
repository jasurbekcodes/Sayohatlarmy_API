from django.db import models
from apps.main.models import BaseModel, Image

from ckeditor.fields import RichTextField


class Category(BaseModel):
    name = models.CharField(max_length=200)
    icon = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/countries/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Davlatlar'
        verbose_name = 'Davlat'


class Destination(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/destinations/')
    country = models.ForeignKey(
        Country, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def lowest_price(self):
        try:
            tours = self.tours.order_by('price')
            return tours.first().price
        except:
            return 0

    class Meta:
        ordering = ('-id', )


class HotelFacility(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hotel(BaseModel):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    stars = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='hotels/')
    address = models.CharField(max_length=100)
    facilities = models.ManyToManyField(HotelFacility, blank=True)
    hotel_class = models.CharField(max_length=100, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name


class Tour(BaseModel):
    name = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/tours/')
    destinations = models.ManyToManyField(
        Destination, blank=True, related_name='tours')
    countries = models.ManyToManyField(Country, blank=True)
    categories = models.ManyToManyField(Category, blank=True)
    hotels = models.ManyToManyField(Hotel, blank=True)
    hit_count = models.PositiveIntegerField(default=0)
    price_list = RichTextField(blank=True, null=True)
    programm = RichTextField(blank=True, null=True)
    visa = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.name


    @property
    def rating(self):
        reviews = self.reviews.all()
        if not reviews:
            return 0
        rating_sum = reviews.aggregate(models.Sum('rating'))
        rating = rating_sum['rating__sum'] / len(reviews)
        return rating
        
        

    class Meta:
        ordering = ('-id', )


class Food(BaseModel):
    has_breakfast = models.BooleanField(default=True)
    has_lunch = models.BooleanField(default=False)
    has_dinner = models.BooleanField(default=False)

    breakfast = models.TextField(blank=True, null=True)
    lunch = models.TextField(blank=True, null=True)
    dinner = models.TextField(blank=True, null=True)

    tour = models.OneToOneField(
        Tour, on_delete=models.CASCADE, related_name='food')


class TourReview(BaseModel):
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField()
    rating = models.PositiveSmallIntegerField(default=1)
    body = models.TextField()
    tour = models.ForeignKey(Tour, models.CASCADE, related_name='reviews')
