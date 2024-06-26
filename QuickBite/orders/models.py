from django.db import models
from datetime import datetime
# Create your models here.
class requestFoodPlace(models.Model) :
    place_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 500)
    owner_username = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100  ,default = 'Admin')
    des = models.CharField(max_length = 500 , default = "hello")
class FoodPlace(models.Model):
    place_name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 500)
    owner_username = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100  ,default = 'Admin')
    place_img = models.ImageField(upload_to='static/assets/img/menu/' , default='static/assets/img/menu/menu-item-1.png')


foodsections = FoodPlace.objects.filter(id  = 2)
class Sections(models.Model)  :
    section_categories = { "S" : "Snacks" , "B"  : "Beverages" , "M" :  "Main Course"}
    place_id  = models.ForeignKey(FoodPlace, on_delete=models.CASCADE  ,default = 2)
    section_name = models.CharField(max_length = 100)
    desc = models.CharField(max_length = 500)
    price_lower = models.IntegerField(default = 0)
    price_higher = models.IntegerField(default = 0)
    section_category = models.CharField(max_length = 2 , choices = section_categories , default = "M")
    img = models.ImageField(upload_to='static/assets/img/menu/' , default='static/assets/img/menu/menu-item-1.png')
class SubSection(models.Model) : 
    section_id  = models.ForeignKey(Sections, on_delete=models.CASCADE)
    subsection_name = models.CharField(max_length = 100)
    price = models.IntegerField(default = 0)
    sub_img = models.ImageField(upload_to='static/assets/img/menu/' , default='static/assets/img/menu/menu-item-1.png')

class Order(models.Model) : 
    order_username = models.CharField(max_length = 100)
class Ordercontent(models.Model) :
    order_id = models.ForeignKey(Order , on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    subsection_id = models.ForeignKey(SubSection , on_delete = models.CASCADE)

class order_log(models.Model) :
    order_username = models.CharField(max_length = 100)
    date = models.DateTimeField(default=datetime.now, blank=True)
    location = models.CharField(max_length= 150)
    phone_number = models.CharField(max_length=21)
    delivery_status  = models.BooleanField(default = False)

class order_log_data(models.Model)  :
    order_log_id = models.ForeignKey(order_log , on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 0)
    subsection_id = models.ForeignKey(SubSection , on_delete = models.CASCADE)
    








