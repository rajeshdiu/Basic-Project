from django.db import models

from django.contrib.auth.models import AbstractUser


class customUser(AbstractUser):
    
    GENDER=[
        ('male',"Male"),
        ('female',"Female"),
        ('others',"Others"),
    ]
    
    USER=[
        ('viewers','Viewers'),
        ('blooger','Blooger')
    ]
    
    user_type=models.CharField(choices=USER,max_length=100,null=True)

    Gender=models.CharField(choices=GENDER, max_length=100,null=True)
    Age=models.PositiveIntegerField(null=True)
    Contact_No=models.CharField(max_length=100,null=True)
    
    def __str__(self):  
        
        return f"{self.username}-{self.Age}"
    