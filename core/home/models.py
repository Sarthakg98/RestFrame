from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class Student(BaseModel):
    name=models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True,default=None)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    is_active = models.BooleanField(default=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    
    def __str__(self):
        return f"Student: {self.name}, Roll: {self.roll}, City: {self.city}, Course: {self.course.name}"
    
#Create a course model
class Course(BaseModel):
    name= models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Course: {self.name}, Duration: {self.duration}, Fee: {self.fee}"
    
