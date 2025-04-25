from django.db import models 

# Create your models here.
class staff(models.Model):
   
   staff_id=models.IntegerField(primary_key=True)
   staff_name=models.CharField(max_length=50,blank=True,null=True)      
   email=models.EmailField   
   phone=models.IntegerField    
   role_id=models.IntegerField     
   hotel_id= models.IntegerField


