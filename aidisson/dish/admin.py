from django.contrib import admin

from .models import Dish, Ingredient

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
	readonly_fields = ('carb_total', 'fat_total', 'protein_total')



admin.site.register(Ingredient)