from rest_framework import serializers
from .models import Student, Course

def starts_with_r(value):
    "Ensure name starts with 'R'"
    if not value.lower().startswith('r'):
        raise serializers.ValidationError('Name must start with "R".')
    
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=['id', 'name', 'duration', 'fee']     

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model=Student
        fields=['id', 'name', 'roll', 'city','course']
        
    def validate_roll(self, value):
        "Ensure roll number is positive"
        if value <=0:
            raise serializers.ValidationError("Roll number must be a positive integer.") 
        return value
    
