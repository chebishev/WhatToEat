from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import Meal

# Register your models here.
# changing admin header
admin.site.site_header = "What To Eat - Admin Panel"
# changing admin title
admin.site.site_title = "What to eat?"


class MealResource(resources.ModelResource):
    class Meta: 
        model = Meal


class MealAdmin(ImportExportActionModelAdmin):
    resource_class = MealResource


admin.site.register(Meal, MealAdmin)