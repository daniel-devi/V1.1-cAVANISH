from django.db import models
from django.contrib.auth.models import User
import datetime
from datetime import timedelta
import uuid


# Create your models here.


class Rooms (models.Model):
    room_name = models.CharField(help_text = "Room Name",max_length=50)
    room_number = models.SlugField()
    rent_amount = models.FloatField()
   #Metadata
    class Meta :
       ordering = ['room_number']

    #eMethods
    
    def __str__(self):
       return f" {self.room_name}"
   


class Payments(models.Model):
    name = models.TextField(default = "Payment")
    payment_made_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    room = models.ManyToManyField(Rooms, related_name='payments')
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    amount_payed = models.PositiveIntegerField()
    rent_date_start = models.DateField()
    rent_date_end = models.DateField()
    date_payed = models.DateTimeField()
    PAY_METHODS = {
        'Online': "Through our Application",
        "Cash": "Cash Deposit"
    }
    payment_method = models.CharField(max_length=99, choices=PAY_METHODS)
    payment_remark = models.TextField(max_length= 999, default="Thanks For Using Cavanish Home")
    
    #Methods
    def __str__(self):
       return f" {self.name}"
   
   


class House (models.Model):
    name = models.CharField(max_length = 50 ,blank=False)
    location = models.CharField(max_length= 9999, blank=False)
    description = models.CharField(max_length = 99999, blank=False)
    rooms_total = models.IntegerField(blank=False)
    rooms = models.ManyToManyField(Rooms)
    annoucements = models.CharField(max_length = 9999)
    #images
    house_image1 = models.ImageField(upload_to='uploads', blank=True, height_field=700, width_field=700)
    house_image2 = models.ImageField(upload_to='uploads', blank=True, height_field=700, width_field=700)
    house_image3 = models.ImageField(upload_to='uploads', blank=True, height_field=700, width_field=700)
    house_image4 = models.ImageField(upload_to='uploads', blank=True, height_field=700, width_field=700)
    house_image5 = models.ImageField(upload_to='uploads', blank=True, height_field=700, width_field=700)
    
    
    def __str__(self):
       return f" {self.name}"
    


class Complains(models.Model):
    tenant = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.TextField(max_length = 99)
    content = models.CharField(max_length=9999)
    
    def __str__(self):
        return f"{self.name}"