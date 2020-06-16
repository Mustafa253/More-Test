from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404

# Create your models here.
class PythonType(models.Model):
    pythontypename=models.CharField(max_length=255)
    pythondescription=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.pythontypename
    
    class Meta:
        db_table='pythontype'
        verbose_name_plural='pythontypes'

class Product(models.Model):
    productname=models.CharField(max_length=255)
    pythontype=models.ForeignKey(PythonType,on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    productprice=models.DecimalField(max_digits=10, decimal_places=2)
    productentrydate=models.DateField()
    productURL=models.URLField(null=True, blank=True)
    productdescription=models.TextField(null=True, blank= True)

    def __str__(self):
        return self.productname

    def  memberDiscount(self):
         discount= .05
         return float(self.productprice)  * discount
    
    def discountedPrice(self):
        discount=self.memberDiscount()
        return float(self.productprice)-discount
    
    class Meta: 
         db_table='product'
         verbose_name_plural='products'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=225)
    reviewdate=models.DateField()
    product=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
    user=models.ManyToManyField(User)
    rating=models.SmallIntegerField()
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'


