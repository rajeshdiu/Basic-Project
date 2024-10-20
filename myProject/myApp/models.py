from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('viewers','Viewers'),
        ('creator','Creator'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic' ,null=True)
    
    def __str__(self):  
        
        return f"{self.username}"
    
class viewersProfileModel(models.Model):
    
    INTEREST=[
        ('desserts','Desserts'),
        ('vegan_recipes','VeganRecipes'),
    ]
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='viewersProfile')
    Interests=models.CharField(choices=INTEREST, max_length=100,null=True)
    
    def __str__(self):
        return f"{self.user.username}"
    
    
class creatorProfileModel(models.Model):
    
    SPECIALIST=[
        ('desserts','Desserts'),
        ('vegan_recipes','VeganRecipes'),
    ]
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='creatorsProfile')
    Specialties=models.CharField(choices=SPECIALIST,max_length=100,null=True)
    Followers=models.PositiveIntegerField(max_length=100,null=True)
    Achievements=models.CharField(max_length=100,null=True)
    Bio=models.TextField(max_length=100,null=True)
    
    
    def __str__(self):
        return f"{self.user.username}"
    
    
class RecipeModel(models.Model):
    
    TAG=[
        ('Vegetarian','Vegetarian'),
        ('Non_Vegetarian','Non-Vegetarian')
    ]
    CATEGORY=[
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
    ]
    DIFFICULTY=[
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard'),
    ]
    
    user=models.ForeignKey(customUser, on_delete=models.CASCADE, related_name='recipemodel')
    
    Category=models.CharField(choices=CATEGORY,max_length=100,null=True)
    Difficulty=models.CharField(choices=DIFFICULTY,max_length=100,null=True)
    Tag=models.CharField(choices=TAG,max_length=100,null=True)

    title=models.CharField(max_length=100,null=True)
    
    ingredients=models.TextField(null=True)
  
    instructions=models.TextField(null=True)
    
    prep_time=models.PositiveIntegerField(null=True)
    cooking_time=models.PositiveIntegerField(null=True)
    total_time=models.PositiveIntegerField(null=True)
    nutrition=models.TextField(null=True)
    image=models.ImageField(upload_to='Media/Recipe_Image' ,null=True)
    calories=models.PositiveIntegerField(null=True)
    
    def __str__(self):
        return f"{self.user.username}- {self.title}"
   