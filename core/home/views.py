

# Create your views here.

# @api_view(['POST'])
# def home(request):
#     return Response({'status': 200, 'message': 'Hello from django rest framework'})


#class based view
# from rest_framework.generics import ListCreateAPIView
# from .models import Student
# from .serializers import StudentSerializer

# class StudentListCreateView(ListCreateAPIView):
#     queryset =Student.objects.all()
#     serializer_class = StudentSerializer
    
# from rest_framework.generics import RetrieveUpdateAPIView    
# from .models import Student
# from .serializers import StudentSerializer


# #API VIEW
# #MODEL VIEWSET

# class StudentUpdateView(RetrieveUpdateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer


# api_views for crud for student model

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer
from rest_framework import viewsets

@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        students= Student.objects.all()
        serializer =StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PATCH', 'DELETE'])
def student_detail(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)            
        
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer    