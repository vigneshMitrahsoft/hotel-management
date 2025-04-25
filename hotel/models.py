from django.db import models


class Hotel(models.Model):
    hotel_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 200)
    email = models.EmailField()
    phone = models.CharField(max_length = 10)

