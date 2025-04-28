from django.db import models

class Staff(models.Model):
   staff_id=models.BigIntegerField(primary_key=True)
   staff_name=models.CharField(max_length=50,blank=True,null=True )
   email=models.EmailField()
   phone=models.BigIntegerField()
   role_id=models.BigIntegerField()
   hotel_id= models.BigIntegerField()
   created_at=models.DateField(auto_now=True)
   updated_at=models.DateField(auto_now=True)
   created_by=models.IntegerField(null=True)
   updated_by=models.IntegerField(null=True)
   
   def __str__(self):
      return self.staff_name

# class role(models.Model):
#    role_name = models.CharField(max_length=50,blank=True,null=True)
#    role_id = models.IntegerField(primary_key=True)

#    def __str__(self):
#       return self.role_name
    
# class amenities(models.Model):
#    amenities_id = models.IntegerField(primary_key=True)
#    amenities_name  = models.CharField(max_length=50,blank=True,null=True)
#    description = models.TextField()

#    def __str__(self):
#       return self.amenities_name
    

# class room_amenties(models.Model):
#    room_amenties_id = models.IntegerField(primary_key=True)
#    room_id = models.IntegerField(primary_key=True)
#    amenities_id =  models.IntegerField(primary_key=True)
