from django.contrib import admin
from app1.models import car

# Register your models here.

@admin.register(car)
class carAdmin(admin.ModelAdmin):
    list_display =  ['id','c_name','color','price']