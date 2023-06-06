from django.conf import settings
from django.db import models


class Post(models.Model):
    car_plate = models.CharField(max_length=50,unique=True,null=True,blank=False)
    car_name = models.CharField(max_length=50,null=True,blank=False)
    car_owner = models.CharField(max_length=50,null=True,blank=False)
    car_color = models.CharField(max_length=50,null=True,blank=False)
    published_date = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return self.car_plate