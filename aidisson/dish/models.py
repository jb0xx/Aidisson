from django.db import models

# from usda_nutrition.models import 

# Create your models here.

class Ingredient(models.Model):
	name 			= models.CharField(max_length=30)
	carb_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of carbs per 100g')
	fat_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of fat per 100g')
	fiber_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of fiber per 100g')
	protein_comp	= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of protein per 100g')
	sugar_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of sugar per 100g')
	water_comp		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of water per 100g')
	serving_size	= models.DecimalField(max_digits=7, decimal_places=3, default=0, help_text='recommended serving size for this ingredient in grams')


	def __str__(self):
		return self.name



class Dish(models.Model):
	name 			= models.CharField(max_length=100)
	ingredients 	= models.ManyToManyField(Ingredient)
	num_servings 	= models.CharField(max_length=100, help_text='number of servings of each ingredient in this dish, delimited by commas')
	carb_total		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='total net carbs in grams')
	fat_total		= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='total fat in grams')
	protein_total	= models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='total protein in grams')


	def __str__(self):
		return self.name


	def save(self, *args, **kwargs):
		super(Dish, self).save(*args, **kwargs)
		serving_list = self.num_servings.split(',')
		self.carb_total = 0
		self.fat_total = 0
		self.protein_total = 0
		for n, i in zip(serving_list, self.ingredients.all()):
			self.carb_total += int(n) * i.carb_comp * i.serving_size / 100
			self.fat_total += int(n) * i.fat_comp * i.serving_size / 100
			self.protein_total += int(n) * i.protein_comp * i.serving_size / 100
		super(Dish, self).save(*args, **kwargs)


	class Meta:
		verbose_name_plural = 'dishes'
