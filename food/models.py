from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    image = models.ImageField(upload_to='food_menu/',default='food_menu/single_food_1.png')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ManyToManyField(Category)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return self.name

class Chef(models.Model):
    image = models.ImageField(upload_to='chefs/',default='chefs/chefs_1.png')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    class Meta:
        ordering = ['-title']

    def __str__(self):
        return self.name

class Reservation(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    persons = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(20)])
    phone = models.CharField(max_length=30)
    date = models.DateField()
    time_slot = models.CharField(max_length=30)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date','created_at']


    def __str__(self):
        return f"{self.name} - {self.date} - {self.time_slot}"