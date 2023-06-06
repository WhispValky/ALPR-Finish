from dataclasses import field
import django_filters
from .models import Post

class Car_Plate_Filter(django_filters.FilterSet):
    class Meta:
        model = Post
        fields = {'car_plate': ['icontains'], 'car_name': ['icontains'],
        }