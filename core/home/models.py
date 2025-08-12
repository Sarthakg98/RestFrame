from django.db import models
import uuid

# Create your models here.
class Student(models.Model):
    id= models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True,default=None)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    is_active = models.BooleanField(default=True)
    
#COURSES

#POSTGRSEQL
#ID should be a uuid