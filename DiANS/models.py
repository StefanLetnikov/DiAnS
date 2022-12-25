from django.db import models
from django.contrib.auth.models import User
import math

# Create your models here.
class Manufacturer(models.Model):
    manufacturer_Name = models.CharField(max_length=30)

    def __str__(self):
        return self.manufacturer_Name


class Product(models.Model):
    product_Name = models.CharField(max_length=30)
    product_Price = models.CharField(max_length=10)
    #product_Manufacturer = models.CharField(max_length=20)
    #product_CoverImage = models.ImageField(upload_to="cover_images/", null=True, blank=True)

    def __str__(self):
        return self.product_Name + " " + self.product_Price + "$"



class Shop(models.Model):
    shop_Name = models.CharField(max_length=50)
    shop_Address = models.CharField(max_length=50)
    shop_City = models.CharField(max_length=25)
    shop_Longitude = models.CharField(max_length=25)
    shop_Latitude = models.CharField(max_length=25)
    shop_ContactNumber = models.CharField(max_length=12, null=True, blank=True)
    # customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    # ShopUserDistance = models.FloatField(blank=True,null=True)
    #
    def __str__(self):
        return self.shop_Name + " / " + self.shop_City + " - " + self.shop_Address



class ManufacturerProduct(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
