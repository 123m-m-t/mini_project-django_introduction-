from django.db import models

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
