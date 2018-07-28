from django.db import models

from users.models import Trainee
# from usda_nutrition.models import 

# Create your models here.

class Ingredient(models.Model):
    name            = models.CharField(max_length=30)
    carb_comp       = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of carbs per 100g')
    fat_comp        = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of fat per 100g')
    fiber_comp      = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of fiber per 100g')
    protein_comp    = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of protein per 100g')
    sugar_comp      = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of sugar per 100g')
    water_comp      = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='grams of water per 100g')
    serving_size    = models.DecimalField(max_digits=7, decimal_places=3, default=0, help_text='recommended serving size for this ingredient in grams')


    def __str__(self):
        return self.name



class Dish(models.Model):
    name            = models.CharField(max_length=100)
    ingredients     = models.ManyToManyField(Ingredient)
    num_servings    = models.CharField(max_length=100, help_text='number of servings of each ingredient in this dish, delimited by commas')
    carb_total      = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='total net carbs in grams')
    fat_total       = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='total fat in grams')
    protein_total   = models.DecimalField(max_digits=5, decimal_places=3, default=0, help_text='total protein in grams')


    def __str__(self):
        return self.name


    def get_total_calories(self):
        return 4 * (2*self.fat_total + self.protein_total + self.carb_total)


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



class Meal(models.Model):
    trainee     = models.ForeignKey(Trainee, on_delete=models.CASCADE)
    dishes      = models.ManyToManyField(Dish)
    datetime    = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        username = self.trainee.user.username
        date = self.datetime.date()
        time = self.datetime.strftime("%H:%M:%S")
        meal_type = self.determine_type()
        return f"{username}: {date} {meal_type} - {time}"


    def get_total_calories(self):
        total = 0
        for dish in self.dishes.all():
            total += dish.get_total_calories()
        return total


    def determine_type(self):
        if self.get_total_calories() < 400:
            meal_type = 'Snack' 
        else:
            dt = self.datetime.seconds / 60 / 60
            if dt > 18:
                meal_type = 'Dinner'
            elif dt > 12:
                meal_type = 'Lunch'
            elif dt > 4:
                meal_type = 'Breakfast'
            else:
                meal_type = '???'
        return meal_type




