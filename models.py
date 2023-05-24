from django.db import models

# Create your models here.

    
class RoomAvailable (models.Model):
    checkindate = models.DateField()
    checkoutdate= models.DateField()

    def __date__(self):
        return self.status+ ","+ self.checkindate + ","+self.checkoutdate
    
class Clientsinfo(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    date= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name + ","+str(self.phone)