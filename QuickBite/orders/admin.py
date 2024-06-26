from django.contrib import admin
from .models import Sections
from .models import SubSection
from .models import FoodPlace
from .models import Order
from .models import Ordercontent
from .models import order_log
from .models import order_log_data
from .models import requestFoodPlace
# Register your models here.
admin.site.register(Sections)
admin.site.register(SubSection)
admin.site.register(FoodPlace)
admin.site.register(Order)
admin.site.register(Ordercontent)
admin.site.register(order_log)
admin.site.register(order_log_data)
admin.site.register(requestFoodPlace)