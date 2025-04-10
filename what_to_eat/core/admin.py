from django.contrib import admin
from .models import Meal

# Register your models here.
# changing admin header
admin.site.site_header = "What To Eat - Admin Panel"
# changing admin title
admin.site.site_title = "What to eat?"


admin.site.register(Meal)