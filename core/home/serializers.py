from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id', 'name', 'roll', 'city']
        
    def validate_roll(self, value):
        "Ensure roll number is positive"
        if value <=0:
            raise serializers.ValidationError("Roll number must be a positive integer.") 
        return value