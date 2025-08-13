

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
from django.db.models import Avg, Count, F

#Aggregate endpoint
@api_view(['GET'])
def aggregate_view(request):
    data = Student.objects.aggregate(
        avg_roll=Avg('roll'),
        total_students=Count('id')
    )
    return Response(data, status=status.HTTP_200_OK)

#Annotate endpoint
@api_view(['GET'])
def annotate_view(request):
    courses= Course.objects.annotate(
        total_students=Count('students'),
        avg_roll=Avg('students__roll'),
    ).values('name', 'total_students', 'avg_roll')
    return Response(list(courses), status=status.HTTP_200_OK)

# FILTER endpoint
@api_view(['GET'])
def filter_view(request):
    # Example: Filter students with roll >= 2
    students = Student.objects.filter(roll__gte=2).values('name', 'roll', 'city', 'course__name')
    return Response(list(students))

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
    
    
@api_view(['GET'])
def select_related_view(request):
    students= Student.objects.select_related('course').values(
        'name', 'roll', 'course__name', 'course__duration', 'course__fee'
        ) 
    return Response(list(students), status=status.HTTP_200_OK)

@api_view(['GET'])
def prefetch_related_view(request):
    courses = Course.objects.prefetch_related('students').values(
        'name', 'duration', 'students__name', 'students__roll'
    )
    return Response(list(courses))   