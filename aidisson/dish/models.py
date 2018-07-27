from django.db import models

# from usda_nutrition.models import 

# Create your models here.




class Ingredient(models.Model):
	name 			= models.CharField(max_length=30)
	carb_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='carbs per 100g')
	fat_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='fat per 100g')
	protein_comp	= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='protein per 100g')
	water_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='water per 100g')
	serving_size	= models.DecimalField(max_digits=7, decimal_places=3, default=0, help_text='recommended serving size for this food in grams')


	def __str__(self):
		return self.name