from django.db import models

# Create your models here.       
class rooms(models.Model):
    room_number = models.IntegerField()
    status = models.CharField(max_length=100)
    price = models.DecimalField()
    
    def __str__(self):
        return self.price
    
    class Meta:
        db_table = 'room'
