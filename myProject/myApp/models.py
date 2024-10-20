from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('viewers','Viewers'),
        ('creator','Creator'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    
    
    def __str__(self):  
        
        return f"{self.username}"
    
class viewersProfileModel(models.Model):
    
    INTEREST=[
        ('desserts','Desserts'),
        ('vegan_recipes','VeganRecipes'),
    ]
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='viewersProfile')
   
    
    def __str__(self):
        return f"{self.user.username}"
    
    
class creatorProfileModel(models.Model):
    
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='creatorsProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    
  