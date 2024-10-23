from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):   
        
        return f"{self.username}"
    
class seekerProfileModel(models.Model):
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='seekerProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    
    
class recruiterProfileModel(models.Model):
    
   
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='recruiterProfile')
   
    def __str__(self):
        return f"{self.user.username}"
    
  