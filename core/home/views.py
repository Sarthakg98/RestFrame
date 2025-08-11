from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

# @api_view(['POST'])
# def home(request):
#     return Response({'status': 200, 'message': 'Hello from django rest framework'})


#class based view
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer

class StudentListView(ListAPIView):
    queryset =Student.objects.all()
    serializer_class = StudentSerializer
    
